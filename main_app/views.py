from django.shortcuts import render
from .models import Auto

def index(request):
    autos = Auto.objects.all()
    return render(request,'index.html',{"autos":autos})

