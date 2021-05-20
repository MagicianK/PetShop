from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Main'),
    path('product/<int:id>', views.to_product, name = 'buy'),
    path('search/', views.search, name = 'search'),
    path('register/', views.register, name = 'register'),
    path('user_account_page/', views.load_account_page, name = 'user_account_page'),
    path('logout/', views.log_out, name='logout'),
    path('loggedout/', views.logged_out, name='logged_out')
]
