from rest_framework import serializers
from mypage.models import Plan
from account.models import User

class friendSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')
