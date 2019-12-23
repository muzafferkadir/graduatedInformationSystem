from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserTable

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserTable
        fields = ['first_name','last_name','username', 'email','birthday','student_no','tc_no','department'
                    ,'graduate_year','foreign_languages','certificates','telephone','image',]

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserTable
        fields = ('username', 'email')