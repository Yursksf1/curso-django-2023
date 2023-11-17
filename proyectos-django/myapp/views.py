from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)

def index(request):
    return HttpResponse('Hola mundo')

def home(request):
    return HttpResponse('<h1> Bienvenido al curso de django 2023 </h1>')