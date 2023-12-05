from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index ),
    path('Horas', views.Horas ),
    path('Horas1', views.tabla_1 ),
    path('Horas2', views.Horas ),
]