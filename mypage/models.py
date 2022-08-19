import profile
from django.db import models
from account.models import User

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    present_time = models.IntegerField(null=True)
    isDone = models.BooleanField(default=False)
    promise_time = models.IntegerField(null=True)
    title = models.CharField(max_length=30,blank=False)
    place_name = models.CharField(max_length=30)
    place_id = models.IntegerField()
    max_count=models.IntegerField()
    reward=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    count=models.IntegerField(default=1)
    joiner = models.ManyToManyField(User,related_name='join')
    profile_image = models.URLField(null=True)

    def __str__(self):
        return self.title