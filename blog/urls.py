from django.urls import path
from .import views

urlpatterns = [
    path('lista1', views.lista_usuarios, name='lista1'),
    path('formulario1', views.formulario1, name='formulario1'),
    path('home', views.home, name='Home'),
    path('formulario2', views.formulario2, name='formulario2'),
    path('lista2', views.lista_usuarios2, name='lista2'),
    path('contraseña', views.contraseña, name='contraseña'),
    path('formulario3', views.formulario4, name='formulario3'),
]