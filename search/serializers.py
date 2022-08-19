from rest_framework import serializers
from mypage.models import Plan
from account.models import User

class friendSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class listSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('place_name','name','title','promise_time','reward','max_count')