from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'avatar',
        'bio',
        'phone',
        'age',
        'created_at',
    ]















