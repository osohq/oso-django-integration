from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.backends import ModelBackend

from .models import *

# Register your models here.
admin.site.register(User, UserAdmin)

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = User(username=username, password="")
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
