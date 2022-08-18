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
        plan.user = request.user #
        plan.name = request.user.username #
  
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
            
