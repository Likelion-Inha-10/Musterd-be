from django.db import models


class Plan(models.Model):
    # email = models.ForeignKey(User)
    present_time = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField()
    promise_time = models.IntegerField()
    title = models.CharField(blank=False)
    place_name = models.CharField()
    place_id = models.IntegerField()
    max_count=models.IntegerField()
    reward=models.CharField()
    name=models.IntegerField()
    category=models.CharField()
    