from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Bienvenido a Automart</h1>')

# Create your views here.
