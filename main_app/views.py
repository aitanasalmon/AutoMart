from django.shortcuts import render

def index(request):
  
   return render(request,'index.html',{"autos":autos})

class Auto:
    def __init__(self,nombre,precio,modelo,color,img_url):
        self.nombre = nombre
        self.precio = precio 
        self.modelo = modelo 
        self.color = color 
        self.img_url = img_url

autos = [
    Auto("VW Jetta",145000,2018,"Gris","https://blogmedia.dealerfire.com/wp-content/uploads/sites/209/2018/01/White-2018-Volkswagen-Jetta-Driving-on-a-City-Street_o.jpg"),
    Auto("Lexus",256000,2017,"Blanco","https://cars.usnews.com/static/images/Auto/izmo/i2345001/2017_lexus_es_angularfront.jpg"),
    Auto("Futura",0,1954,"Negro","https://www.legacydiecast.com/product_images/mp107-082030.jpg"),
    Auto("Porshe",250000,2010,"Azul","https://www.km77.com/media/fotos/porsche_cayenne_2010_3457_1.jpg"),
    Auto("Mazda 3",200000,2018,"Rojo","https://acs2.blob.core.windows.net/imgcatalogo/l/VA_d317084baa694fd49900e659d4d73008.jpg"),
]
# Create your views here.
