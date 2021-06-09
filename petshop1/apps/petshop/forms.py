from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rating')

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'input-text'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'telephone')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-input'}),
            'telephone': forms.TextInput(attrs={'class': 'text-input'}),
        }

