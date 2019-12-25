from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserTable

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = UserTable
#     list_display =  ['first_name','last_name','username', 'email','birthday','student_no','tc_no','department','telephone']
#     list_display_links =['email']
#     fieldsets = UserAdmin.fieldsets + (
#             ({'fields': ['birthday','student_no','tc_no','department','graduate_year','foreign_languages',
#                         'certificates','telephone','image',]}),
#     )
# #admin add form
admin.site.register(UserTable)