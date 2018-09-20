from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):  # N - 1:N 관계에서 N
    # author = models.CharField(max_length=30)
    author = models.ForeignKey('CustomUser', on_delete='CASCADE')
    title = models.CharField(max_length=50)  # CharField는 max_length 필수!
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class CustomUser(User):  # 1 - 1:N 관계에서 1 # django가 제공하는 User 모델을 상속하는것
    # username
    # email
    # password
    # is_authenticated
    is_author = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    writer = models.ForeignKey(CustomUser, on_delete='CASCADE')
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self): # 오버라이딩하는 것이여
        return self.contents