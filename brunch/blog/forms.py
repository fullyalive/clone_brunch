from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import CustomUser, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'contents']
        widgets = {
            'contents': SummernoteWidget(),
            # 'contents': SummernoteInplaceWidget(),
        }
class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email','name','password']
