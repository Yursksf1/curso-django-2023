from django.contrib import admin
from django.urls import path, include
from myapp import views


app_name = "app"
urlpatterns = [
    path('', views.index, name='index'),
    path('My_Navidad', views.My_Navidad, name='my_navidad'),
    path('Cancion', views.Canciones, name='canciones' ),
    path('Cocina', views.Cocina, name='cocina' ),
    path('Regalos', views.Regalos, name='regalos'),    
]