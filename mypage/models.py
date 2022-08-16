from django.db import models
from account.models import User

class Plan(models.Model):
    email = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    present_time = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)
    promise_time = models.IntegerField()
    title = models.CharField(max_length=30,blank=False)
    place_name = models.CharField(max_length=30)
    place_id = models.IntegerField()
    max_count=models.IntegerField()
    reward=models.CharField(max_length=30)
    name=models.IntegerField()
    category=models.CharField(max_length=30)
    