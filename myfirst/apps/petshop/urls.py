from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'Main'),
    path('search/', views.search, name = 'search')
]
