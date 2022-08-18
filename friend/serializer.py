from rest_framework import serializers
from mypage.models import Plan

#친구의 약속목록을 모두 가져옵니다.
class friendsPlanSerializer(serializers.ModelSerializer):
    is_mine = serializers.SerializerMethodField()
    
    class Meta:
        model = Plan
        fields = ('id','isDone','title','promise_time','is_mine')

    def get_is_mine(self, obj):

        if obj.user == self.context['request'].user:
            return True
        else:
            return False