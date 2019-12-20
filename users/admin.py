from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserTable

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserTable
    list_display = ['email', 'username',]
    list_display_links =['email']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('birthday','student_no','tc_no','department','telephone','image',)}),
    )

admin.site.register(UserTable, CustomUserAdmin)