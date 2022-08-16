from rest_framework import serializers
from .models import Plan

class planSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('title', 'category','place_name','place_id','promise_time','max_count','user')
        extra_kwargs = {
            'isDone': {'write_only': True},
        }

class promiseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        # fields = ('name','place_name','reward','max_count','count')
        fields = ('name','place_name','max_count','count')