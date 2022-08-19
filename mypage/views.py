from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .models import Plan
from account.models import User
from .serializers import planSerializers, promiseSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from http import HTTPStatus
from rest_framework import generics
from rest_framework.decorators import api_view
from friend.models import UserPoint
# <class promise>
# GET /mypage/promise_place/:plan_id
# PATCH /mypage/finish/:plan_id
# DELETE /mypage/delete/:plan_id
# POST /mypage/create/plan

# <class myplan>
# GET /mypage

class promise(APIView):
    # 새로운 플랜 생성
    def post(self,request, *args, **kwargs):
        # myuser=User.objects.get(pk=request.user.id)
        plan=Plan()
        plan.title=request.data["title"]
        plan.category=request.data["category"]
        plan.place_name=request.data["place_name"]
        plan.place_id=request.data["place_id"]
        plan.promise_time=request.data["promise_time"]
        plan.max_count=request.data["max_count"]
        plan.count = 1
        plan.user = request.user #
        plan.name = request.user.username #
        plan.profile_image = request.user.profile_image
  
        # Plan.name=user.objects.name
        plan.save()
        # planse = planSerializers(plan)
        return Response(status=HTTPStatus.OK) #
        # return Response({"message": "일정 저장 완료!"}, status=200)
        # return Response(planse.data)

    # 해당 플랜의 장소와 약속 내용들을 조회  
    def get(self,request, plan_id):
        promise_info=Plan.objects.get(id=plan_id)
        # 일정 정보 확인
        # plan.writer.id==request.user.id
        if promise_info is not None:
            serializer=promiseSerializers(promise_info)
            return Response(serializer.data, status=200)
        
        # 존재하지 않는 일정인 경우
        else:
            return Response({"message": "일정 정보가 없음"}, status=404)

    # plan_id에 해당하는 일정을 삭제
    def delete(self,request,**kwargs):
        if kwargs.get('plan_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            plan_id = kwargs.get('plan_id')
            plan_object = Plan.objects.get(id=plan_id)
            plan_object.delete()
            return Response({"message":"삭제 완료"}, status=204)

            # serializer = CommentSerializer(주석, 데이터=request.data, 부분=참)

    # plan_id에 해당하는 플랜을 완료 처리 (isDone을 False->True로 변경)
    def patch(self,request,plan_id):
        plan = get_object_or_404(Plan, id=plan_id)
        plan.isDone = True
        plan.save()
        return Response({"message":"일정 수행 완료"})

# class myplan(APIView):

class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all() #객체를 반환하는데 사용
    serializer_class = planSerializers
    lookup_field = 'id'
    
    
# @api_view(['POST']) # plan 작성 완료버튼 누르면 reward 내용까지 저장  프론트에서 reward받아와야함 plan_id도
# def save_with_reward(request,plan_id):
#     plan = Plan.objects.get(pk=plan_id)
#     # plan.reward = request.data['reward']
#     # plan.save()
    
#     for i in (plan.joiner-1): #일단 3개 만들고
#         joiner_UserPoint = UserPoint() #UserPoint 객체 생성
#         nowuser = get_object_or_404(User,pk=plan.joiner[i])
#         joiner_UserPoint.owner = nowuser # UserPoint 객체의 owner필드에 요청한'사람'을 저장 
#         joiner_UserPoint.point = 0
#         joiner_UserPoint.save()
    
#     for j in plan.joiner:
#             friend = get_object_or_404(User,pk=plan.joiner[j])
#             nowuser.friend_id = friend
            
from django.shortcuts import render

import requests
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap
from rest_framework.response import Response
from rest_framework.decorators import api_view
##카카오 API
## region에는 '성산일출봉 전기충전소' 검색명이 들어갈 것임
## page_num은 1~3이 입력될 건데, 한 페이지 당 검색목록이 최대 15개임.
## 만약 page_num이 4이상이 되면 3페이지랑 같은 15개의 결과 값을 가져옴. 그래서 1~3만 쓰는 것임
## 입력 예시 -->> headers = {"Authorization": "KakaoAK f221u3894o198123r9"}
## ['meta']['total_count']은 내가 '성산일출봉 전기충전소'를 검색했을 때, 나오는 총 결과 값. 
## ['meta']['total_count']이 45보다 크면 45개만 가져오게 됨
import os
API_KEY=os.environ.get('API_KEY')

@api_view(['POST'])
def elec_location(request):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': request.data['place_name'],'page': 1}
    
    headers = {"Authorization": f"KakaoAK {API_KEY}"}
    

    places = requests.get(url, params=params, headers=headers).json()['documents']
    total = requests.get(url, params=params, headers=headers).json()['meta']['total_count']
    if total > 45:
        print(total,'개 중 45개 데이터밖에 가져오지 못했습니다!')
    else :
        print('모든 데이터를 가져왔습니다!')
     
    return Response(places)
 

## 이 함수는 위 함수 결과 값(1 ~ 45개) 하나하나 분리해서 저장할 것임
## 1번 결과 값 안에는 1번 충전소 이름, 위도, 경도, 전화번호, 도로명 주소 등이 있는데 각각 배열에 저장
## 우리는 충전소 ID, 충전소 이름, 위도, 경도, 도로명주소, 사이트주소를 저장할 것임

def elec_info(places):
    X = []
    Y = []
    stores = []
    road_address = []
    place_url = []
    ID = []
    for place in places:
        X.append(float(place['x']))
        Y.append(float(place['y']))
        stores.append(place['place_name'])
        road_address.append(place['road_address_name'])
        place_url.append(place['place_url'])
        ID.append(place['id'])

    ar = np.array([ID,stores, X, Y, road_address,place_url]).T
    df = pd.DataFrame(ar, columns = ['ID','stores', 'X', 'Y','road_address','place_url'])
    return df
 

## 여러개으 키워드를 검색할 때 사용할 함수임
## location_name에는 ['성산일출봉 전기충전소, '한림공원 전기충전소', ... ,'모슬포 전기충전소']처럼 배열이 입력

def keywords(location_name):
    df = None
    for loca in location:
        # for page in range(1,4):
            local_name = elec_location(loca, 1)
            local_elec_info = elec_info(local_name)

            if df is None:
                df = local_elec_info
            elif local_elec_info is None:
                continue
            else:
                df = pd.concat([df, local_elec_info],join='outer', ignore_index = True)
    return df
 

##지도로 보여주기

def make_map(dfs):
    # 지도 생성하기
    m = folium.Map(location=[33.4935,126.6266],   # 기준좌표: 제주어딘가로 내가 대충 설정
                   zoom_start=12)

    # 미니맵 추가하기
    minimap = MiniMap() 
    m.add_child(minimap)

    # 마커 추가하기
    for i in range(len(dfs)):
        folium.Marker([df['Y'][i],df['X'][i]],
                  tooltip=dfs['stores'][i],
                  popup=dfs['place_url'][i],
                  ).add_to(m)
    return m
 

 

 

# 위의 4개의 함수를 주피터로 실행하고 아래 코드에 원하는 키워드를 입력하면 지도에 보여줍니다.

## 여기 두 개 키워드처럼 가까운 거리에 있는 키워드를 입력하면 
## 중복해서 전기충전소를 검색할 가능성이 아주 놓기 때문에
## drop_duplicates를 해주고 인덱스 리셋을 해준다

if __name__ == "__main__":   #해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령
    location = ['인하대 스터디카페']
    df = keywords(location)
    df = df.drop_duplicates(['ID'])
    df = df.reset_index()
