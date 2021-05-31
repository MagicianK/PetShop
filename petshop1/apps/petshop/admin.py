from django.contrib import admin
from django.shortcuts import render

from .models import *
from django.contrib.auth.models import User

def createUser(request):
    user = User.objects.create_user('myusername', 'myemail', 'mypassword'),
    return render(request, 'registration/register.html')


admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)
# admin.site.register(Customer)
