from django.shortcuts import render

def index(request):
  
   return render(request,'index.html',{"autos":autos})

class Auto:
    def __init__(self,nombre,precio,modelo,color):
        self.nombre = nombre
        self.precio = precio 
        self.modelo = modelo 
        self.color = color 

autos = [
    Auto("VW Jetta",145000,2018,"Gris"),
    Auto("Lexus",256000,2017,"Blanco"),
    Auto("Futura",0,1954,"Negro"),
    Auto("Porshe",250000,2010,"Azul"),
    Auto("Mazda 3",200000,2018,"Rojo"),
]
# Create your views here.
