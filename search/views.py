from django.shortcuts import render, redirect, get_object_or_404
from mypage.models import Plan
from account.models import User
from .serializers import friendSerializers, listSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from http import HTTPStatus
from rest_framework import generics, status

class search_friend(APIView):
    def get(self, request):
        queryset = User.objects.filter(username__contains = request.data['name']) # 언더바 2개임
        serializer_class = friendSerializers(queryset, many=True)
        serialized_data=serializer_class.data
        return Response(serialized_data)

class search_category(APIView):
    def get(self, request):
        queryset = Plan.objects.filter(category="카페")
        serializer1= listSerializers(queryset, many=True)
        queryset = Plan.objects.filter(category="식사")
        serializer2= listSerializers(queryset, many=True)
        
        queryset = Plan.objects.filter(category="스포츠")
        serializer3= listSerializers(queryset, many=True)
        queryset = Plan.objects.filter(category="취미")
        serializer4= listSerializers(queryset, many=True)
        
        queryset = Plan.objects.filter(category="스터디")
        serializer5= listSerializers(queryset, many=True)
        queryset = Plan.objects.filter(category="일상")
        serializer6= listSerializers(queryset, many=True)
 
        newlist=[
            {
            "category":"카페",
            "plan_list":serializer1.data
            },
            {
            "category":"식사",
            "plan_list":serializer2.data
            },
             {
            "category":"스포츠",
            "plan_list":serializer3.data
            },
            {
            "category":"취미",
            "plan_list":serializer4.data
            },
             {
            "category":"스터디",
            "plan_list":serializer5.data
            },
            {
            "category":"일상",
            "plan_list":serializer6.data
            }
        ]
        return Response(newlist,status=200)
