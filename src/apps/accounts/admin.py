from django.contrib import admin
from .models import UserBase


@admin.register(UserBase)
class UserBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
