from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, User, BaseUserManager


class Post(models.Model):  # N - 1:N 관계에서 N
    # author = models.CharField(max_length=30)
    author = models.ForeignKey('CustomUser', on_delete='CASCADE')
    title = models.CharField(max_length=50)  # CharField는 max_length 필수!
    sub_title = models.CharField(max_length=30, blank=True)
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class CustomUserManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):  # 1 - 1:N 관계에서 1 # django가 제공하는 User 모델을 상속하는것
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    writer = models.ForeignKey(CustomUser, on_delete='CASCADE')
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):  # 오버라이딩하는 것이여
        return self.contents
