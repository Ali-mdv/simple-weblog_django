from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(User,UserAdmin)

UserAdmin.fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser', 'is_author',
										 'special_user', 'groups', 'user_permissions')

UserAdmin.list_display += ('is_author', 'is_special')
UserAdmin.list_filter += ('is_author', 'special_user')
