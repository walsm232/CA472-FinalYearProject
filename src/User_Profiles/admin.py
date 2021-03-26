from django.contrib import admin
from .models import UserProfile, Friendship

admin.site.register(UserProfile)
admin.site.register(Friendship)