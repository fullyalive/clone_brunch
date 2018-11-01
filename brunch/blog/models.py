from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Post(models.Model):  # N은 외래키 필요
    # author = models.CharField(max_length=30) #max_length 필수
    author = models.ForeignKey('CustomUser', on_delete='CASCADE')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(
        max_length=30, blank=True)  # blank는 빈 칸으로 제출 가능
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):  # 클래스 만들고 object 호출할 때 써야하는 string 함수
        return self.title


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):  # 상속받는 메소드의 첫인자 self, 자바의 this
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


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=225,
        unique=True,
    )
    name = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    following = models.ManyToManyField('self', blank=True)
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
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):  # 클래스 만들고 object 호출할 때 써야하는 string 함수
        return self.contents
