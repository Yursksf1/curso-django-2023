from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index ),
    path('home', views.home ),
    path('imc', views.imc ),
    path('htxusuario', views.htxusuario ),
]