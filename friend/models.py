import email
from django.db import models
from account.models import User

# Create your models here.
class Friends(models.Model):
    myId = models.ForeignKey(User, on_delete=models.CASCADE)
    friendId = models.EmailField()
    count = models.IntegerField()