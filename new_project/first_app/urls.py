from django.urls import path
from . import views
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
# from django.urls import path
# from django.views.generic import TemplateView 
urlpatterns = [
    path('', views.home, name='home'),
    path('ekpa/', views.ekpa, name='ekpa'),
]