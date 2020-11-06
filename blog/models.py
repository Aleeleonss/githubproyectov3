from django.db import models

# Create your models here.
class Cambiar(models.Model):
      contraseña = models.TextField(max_length=30)
      contraseña2 = models.TextField(max_length=30)
      def __str__(self) :
          return "|contraseña : "+self.contraseña + " | comfirmacion de la contraseña :" + self.contraseña2



class Ingresar(models.Model):
      usuario = models.TextField(max_length=30) 
      contraseña = models.TextField(max_length=30)
      def __str__(self) :
         return "| Usuario :  " +self.usuario +  " | Contraseña :  " + self.contraseña

class Crear(models.Model):
    usuario = models.TextField(max_length=30)
    nombre  = models.TextField(max_length=30)
    contraseña = models.TextField(max_length=30)
    contraseña2 = models.TextField(max_length=30)
    correo = models.TextField(max_length=30)
    telefono = models.TextField(max_length=12)
    def __str__(self) :
        return "  |  Usuario : "+ self.usuario +   "  |  Nombre : " + self.nombre + " |  Contraseña : " + self.contraseña + " |   Contraseña2 :   " + self.contraseña2 + " |   Correo :  " + self.correo + " |  Telefono :   " + self.telefono
