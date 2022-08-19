import profile
from rest_framework import serializers
from django.contrib.auth import get_user_model
import random
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id','profile_image','username','email', 'password', 'univ',)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        username = validated_data.get('username')
        # profile_image = validated_data.get('profile_image')
        univ = validated_data.get('univ')
        point = random.randint(1,100)
        profile_image = "https://www.gravatar.com/avatar/"+f"{random.randint(1,100)}"+"?d=identicon"
        user = User(
            email=email,
            username = username,
            # profile_image = profile_image,
            univ = univ,
            point = point,
            profile_image = profile_image,
            is_qr_scanned = False
        )
        user.set_password(password)
        user.save()
        return user
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','profile_image','name','refresh_token')   
        fields = '__all__' 
        extra_kwargs = {
            'password' : {'write_only' : True},
            'last_login' : {'write_only' : True},
            'is_superuser' : {'write_only' : True},
            'email' : {'write_only' : True},
            'groups':{'write_only' : True},
            'univ':{'write_only' : True},
            'user_permissions' : {'write_only' : True}
        }  
