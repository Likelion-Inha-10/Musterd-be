from rest_framework import serializers
from mypage.models import Plan

#친구의 약속목록을 모두 가져옵니다.
class friendsPlanSerializer(serializers.ModelSerializer):
    class Meta:
        is_mine = serializers.BooleanField()
        model = Plan
        fields = ('isDone','title','promise_time')

    def get_is_mine(self, obj):
        if obj.user == self.context['request'].user:
            return True
        else:
            return False