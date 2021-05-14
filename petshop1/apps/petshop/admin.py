from django.contrib import admin
from django.shortcuts import render

from .models import product
from django.contrib.auth.models import User

def createUser(request):
    user = User.objects.create_user('myusername', 'myemail', 'mypassword'),
    return render(request, 'registration/register.html')


admin.site.register(product)
