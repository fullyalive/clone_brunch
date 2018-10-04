from django.forms import ModelForm
from .models import Post, CustomUser


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'contents']


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password']
