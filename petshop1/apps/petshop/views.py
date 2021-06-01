from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import *
from .forms import RegisterForm
from django.contrib import messages
from django.http import JsonResponse
import json


def search_by_stats(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'Search_by_stats.html', context)


def product_price_asc(request):
    products = Product.objects.order_by('price')

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'Search_by_stats.html', context)


def product_price_desc(request):
    products = Product.objects.order_by('-price')
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'Search_by_stats.html', context)


def product_novelty(request):
    products = Product.objects.all().order_by('-novelty')
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'Search_by_stats.html', context)


def update_rating():
    products = Product.objects.order_by('-rating')
    return products


def index(request):  # this is what user first will see at the beginning
    products = update_rating()

    if request.user.is_authenticated:
        if not request.user.customer:
            Customer.objects.create(
            user=request.user,
            name=request.user.username,
            )
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'products' : products, 'cartItems' : cartItems}
    return render(request, 'Main.html', context)


def to_product(request, id):
    # this function will return id of product to product_info.html after user clicked button 'buy'
    products = Product.objects.filter(Q(id=id))
    return render(request, 'product_info.html', {'products': products})


def search(request):
    search_result = request.GET.get('search')
    matches = Product.objects.filter(Q(name__icontains=search_result))
    if matches:
        return render(request, 'product_info.html', {'products': matches})
    else:
        return render(request, 'searchNotFound.html')


def log_out(request):
    logout(request)
    return redirect('/')


def logged_out(request):
    products = update_rating()
    return render(request, 'registration/logout.html', {'products': products})


def load_account_page(request, id):
    return render(request, 'registration/user_account_page.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('Main')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = RegisterForm()
        return render(request, 'registration/register.html', {"form": form})
@login_required(login_url='login')
def login_user_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Main')
        else:
            messages.info(request, 'Username or password is wrong')

    context = {}
    return render(request, 'registration/user_account_page.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        cartItems = order['get_cart_items']
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
