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
            'body': forms.Textarea(attrs={'class': 'input-text', 'style': 'position: absolute; top: 1vw; left: 18vw; height: 20vw; resize: none;  width: 71vw'}),
            'rating': forms.NumberInput(attrs={'class': 'input-text', 'style': 'position: absolute; width:3vw; left: 14vw; top: 18vw; height: 3vw; text-align:center;', 'placeholder': 'Rating'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'telephone', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-text', 'style': 'position: absolute; top: 8vw; left:2vw; width: 26vw;'}),
            'telephone': forms.TextInput(attrs={'class': 'input-text', 'style': 'position: absolute; top: 8vw; left:31vw; width: 26vw;'}),
            'image': forms.FileInput(attrs={'class': 'input-text', 'style': 'position: absolute; top: 8vw; left:60vw; width: 28vw; background-color: grey'})
        }

