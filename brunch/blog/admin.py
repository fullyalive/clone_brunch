from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, CustomUser, Comment

class PostModelAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'
admin.site.register(Post, PostModelAdmin)
admin.site.register(CustomUser)
admin.site.register(Comment)
