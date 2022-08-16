from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .models import Plan
from account.models import User
from .serializers import planSerializers, promiseSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

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
        # user=User.objects.get(email=User.email)
        plan=Plan()
        plan.title=request.data["title"]
        plan.category=request.data["category"]
        plan.place_name=request.data["place_name"]
        plan.place_id=request.data["place_id"]
        plan.promise_time=request.data["promise_time"]
        plan.max_count=request.data["max_count"]
  
        # Plan.name=user.objects.name
        plan.save()
        return Response({"message": "일정 저장 완료!"}, status=200)

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