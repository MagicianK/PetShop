from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    path('user_page/<int:id>', views.load_account_page, name='mypage'),
    path('user_page/<int:id>/edit', views.edit_account_page, name='edit'),
    path('user_page/<int:id>/current_orders', views.currentOrders, name='currentOrders'),
    path('', views.index, name='Main'),
    path('product/<int:id>', views.to_product, name='buy'),
    path('product/<int:id>/add_comment', views.add_comment, name='comment'),
    path('product/<int:id>/delete_comment', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('loggedout/', views.logged_out, name='logged_out'),
    path('search/search_by_stats/', views.search_by_stats, name='search_by_stats'),
    path('update_item/', views.updateItem, name='update_item'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/search_by_stats/price_asc/', views.product_price_asc, name='price_asc'),
    path('search/search_by_stats/price_desc/', views.product_price_desc, name='price_desc'),
    path('search/search_by_stats/novelty/', views.product_novelty, name='novelty'),
    path('processOrder/', views.processOrder, name='processOrder'),
]
