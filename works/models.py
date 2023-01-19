from django.db import models


class Work(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    n = models.IntegerField()
    result = models.IntegerField()
    elapsed_time = models.CharField(max_length=50)
