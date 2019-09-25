from django.shortcuts import render

def index(request):
   nombre = "VW Jetta"
   modelo = 2018
   precio = 153000
   color = "gris"
  
   dict = {"auto_nombre" : nombre,
            "auto_modelo" : modelo,
            "auto_precio" : precio,
            "auto_color" : color,
   }

   return render(request,'index.html',dict)

# Create your views here.
