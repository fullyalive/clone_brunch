from django.contrib import admin
from .models import Post, CustomUser, Comment
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)
admin.site.register(CustomUser)
admin.site.register(Comment)
