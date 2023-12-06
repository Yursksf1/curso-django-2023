from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index ),
    path('suscriptores', views.suscriptores ),
    path('facturar', views.facturar),
]