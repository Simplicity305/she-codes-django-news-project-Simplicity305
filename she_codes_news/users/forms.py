from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm): #sign up page

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm): #editing existing profile

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

