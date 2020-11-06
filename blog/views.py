from django.shortcuts import render
from django.http import HttpResponse
from .models import Crear, Ingresar, Cambiar
from .forms import Formulario1 , Formulario2, Formulario3

# Create your views here.


##### Recuperar contraseña
def formulario4(request):
    if request.method == 'POST' :
         formulario3 = Formulario3(request.POST) 
         if formulario3.is_valid :
             crear2 = formulario3.save(commit=False)
             crear2.save()
             return render(request,"appblog/ingresado.html")
    else : 
        formulario3 = Formulario3()          
    return render(request, "appblog/formulario3.html",{'form' : formulario3})


def contraseña(request):
    lista1 = Cambiar.objects.all()
    return render(request, "appblog/lista_contraseñas.html", {'lista1' : lista1})


##############



### formulario Ingreso 
def formulario2(request):
    if request.method == 'POST' :
         formulario2 = Formulario2(request.POST) 
         if formulario2.is_valid :
             crear = formulario2.save(commit=False)
             crear.save()
             return HttpResponse('formulario recibido')   
    else : 
        formulario2 = Formulario2()          
    return render(request, "appblog/formulario2.html",{'form' : formulario2})


def lista_usuarios2(request):
    lista = Ingresar.objects.all()
    return render(request, "appblog/lista_persona2.html", {'lista' : lista})
###1

### pag principal
def home(request):
    return render(request, "appblog/index.html")


###Formulario Crear una cuenta 
def lista_usuarios(request):
    lista = Crear.objects.all()
    return render(request, "appblog/lista_persona.html", {'lista' : lista})

def formulario1(request):
    if request.method == 'POST' :
        formulario = Formulario1(request.POST)
        if formulario.is_valid :
            crear = formulario.save(commit=False)
            crear.save()
            return HttpResponse('formulario recibido')    
    else :   
        formulario = Formulario1()
    return render(request, 'appblog/formulario1.html',{'form' : formulario})
###2    