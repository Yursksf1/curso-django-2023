from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)

def index(request):
    return HttpResponse('Hola mundo')