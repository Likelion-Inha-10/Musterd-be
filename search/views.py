from django.shortcuts import render, redirect, get_object_or_404
from mypage.models import Plan
from account.models import User
from .serializers import friendSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from http import HTTPStatus
from rest_framework import generics

class search_friend(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer_class = friendSerializers(queryset, many=True)
        serialized_data=serializer_class.data
        return Response(serialized_data)
