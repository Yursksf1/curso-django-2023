from django.contrib import admin
from django.urls import path, include
from myapp import views


app_name = "app"
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.My_Navidad, name='my_navidad'),
    path('Cancion', views.Canciones, name='canciones' ),
    path('Cocina', views.Cocina, name='cocina' ),
    path('Cocina/<int:id_receta>', views.Cocina_receta, name='cocina_receta' ),
    path('Cocina/create/', views.Cocina_create, name='cocina_create' ),
    path('Regalos', views.Regalos, name='regalos'),    
]