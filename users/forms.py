from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserTable

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserTable
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserTable
        fields = ('username', 'email')