from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'Main'),
    path('product/<int:id>', views.to_product, name = 'buy'),
    path('search/', views.search, name = 'search')
]
