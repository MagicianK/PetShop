from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import product

def index(request):
    template = 'Main.html'
    return render(request, template)

def search(request):
    search_post = request.GET.get('search')

    if search_post:
        products = product.objects.filter(Q(name__icontains=search_post))
    else:
        products = product.objects.all()
    return render(request, 'products.html', {'products' : products})
