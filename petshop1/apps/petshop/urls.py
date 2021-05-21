from django.urls import path
from django.conf.urls import url
from . import views

app_name='petshop'
urlpatterns = [
    path('', views.index, name = 'Main'),
    path('product/<int:id>', views.to_product, name = 'buy'),
    path('search/', views.search, name = 'search'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.log_out, name='logout'),
    path('loggedout/', views.logged_out, name='logged_out'),
    url(r'^user_account_page/(?P<user_id>\d+)/$', views.load_account_page, name='personal_page')
]
