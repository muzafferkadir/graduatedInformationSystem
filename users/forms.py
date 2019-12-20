from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserTable

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserTable
        fields = ['username', 'email','birthday','student_no','tc_no','department','telephone']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserTable
        fields = ('username', 'email')