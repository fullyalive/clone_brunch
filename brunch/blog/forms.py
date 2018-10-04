from django.forms import ModelForm
from .models import Post, CustomUser
from django_summernote.widgets import SummernoteWidget


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'contents']
        widgets = {
            'contents': SummernoteWidget(),
        }


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password']
