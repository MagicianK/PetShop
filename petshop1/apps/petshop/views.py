from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import product
from .forms import RegisterForm
from django.contrib import messages


def update_rating():
    products = product.objects.order_by('-rating')
    return products


def index(request): #this is what user first will see at the beginning
    products = update_rating()
    return render(request, 'Main.html', {'products' : products})


def to_product(request, id): #this function will return id of product to product_info.html after user clicked button 'buy'
    products = product.objects.filter(Q(id = id))
    return render(request, 'product_info.html', {'products' : products})


def search(request):
    search_result = request.GET.get('search')
    matches = product.objects.filter(Q(name__icontains = search_result))
    if(matches):
        return render(request, 'product_info.html', {'products' : matches})
    else:
        return render(request, 'searchNotFound.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

"""def login(request):"""
