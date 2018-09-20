from django.contrib import admin
from .models import Post, CustomUser, Comment

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Comment)