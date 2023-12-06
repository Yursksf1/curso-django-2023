from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.Index ),
    path('Horas', views.Horas ),
    path('Imc', views.Imc ),
    path('Inicio', views.Inicio),
]