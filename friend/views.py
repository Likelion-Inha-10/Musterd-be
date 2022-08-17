from django.shortcuts import render

from mypage.models import Plan
from rest_framework.response import Response
from .serializer import friendsPlanSerializer
from rest_framework import generics

#- 친구의 약속목록을 모두 가져옵니다
#    - parameter {
#    friend-id :Int 친구의 아이디,
#    present_time: 오늘 날짜
#    }

class listPlans(generics.ListCreateAPIView):
    lookup_field = 'id'
    def get(self, request):
        friendId = request.GET.get('friend-id', None)
        presentTime = request.GET.get('present_time', None)
        #GET 요청의 파라미터로 friend-id와 present_time 받음
        #해당 friend-id를 가진 사용자의 약속 중 present_time 후에 있는 약속 목록을 가져옴
        queryset = Plan.objects.filter(user_id=friendId, promise_time__gte=int(presentTime))
        serializer_class = friendsPlanSerializer(queryset, many=True)
        return Response(serializer_class.data, status=201)