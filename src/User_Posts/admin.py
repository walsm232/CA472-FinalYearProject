from django.contrib import admin
from .models import UserPost, Comment, Like

# Register your models here.
admin.site.register(UserPost)
admin.site.register(Comment)
admin.site.register(Like)