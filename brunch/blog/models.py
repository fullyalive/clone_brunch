from django.db import models
from django.utils import timezone


class Post(models.Model):
    creator = models.CharField(max_length=30)  # CharField는 max_length 필수!
    title = models.CharField(max_length=50)
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now())
