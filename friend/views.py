from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from account.serializer import UserSerializer
# from friend.models import UserPoint
from account.models import User
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
        # friendId = request.GET.get('friend-id', None)
        # presentTime = request.GET.get('present_time', None)
        friendId = request.data['friend_id']
        presentTime = request.data['present_time']
        #GET 요청의 파라미터로 friend-id와 present_time 받음
        #해당 friend-id를 가진 사용자의 약속 중 present_time 후에 있는 약속 목록을 가져옴
        queryset = Plan.objects.filter(user_id=friendId, promise_time__gte=int(presentTime))
        serializer_class = friendsPlanSerializer(queryset, many=True)
    
        return Response(serializer_class.data, status=201)


@api_view(['POST'])
def join(request,plan_id):  # 내가 plan에 동참 누르면 plan의 주인의 point가 1 증가
    
    plan = get_object_or_404(Plan,pk=plan_id)
    user = get_object_or_404(User,pk=plan.user.id)
    user.point+=1
    user.save()
   
    return Response(status=200)
    
class RankList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-point')
    serializer_class = UserSerializer
    lookup_field = 'id'
    

    