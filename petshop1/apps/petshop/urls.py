from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('user_page/<int:id>', views.load_account_page, name='mypage'),
    path('', views.index, name='Main'),
    path('product/<int:id>', views.to_product, name='buy'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('loggedout/', views.logged_out, name='logged_out'),
    path('search/search_by_stats/', views.search_by_stats, name='search_by_stats')
]
