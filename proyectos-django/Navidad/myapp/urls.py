from django.contrib import admin
from django.urls import path, include
from myapp import views




urlpatterns = [
    path('', views.index),
    path('My_Navidad', views.My_Navidad ),
    path('Canciones', views.Canciones ),
    path('Cocina', views.Cocina ),
    path('Regalos', views.Regalos),
    

    
]