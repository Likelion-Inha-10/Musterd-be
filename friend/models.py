from django.db import models
from account.models import User


# Create your models here.
class Friends(models.Model):
    myId = models.ForeignKey(User, on_delete=models.CASCADE)
    friendId = models.EmailField()
    count = models.IntegerField()
    
    
class UserPoint(models.Model):
    owner = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='owner')
    friend_id = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='friend')
    point = models.IntegerField(null=True)

