from django import forms 

from .models import Crear, Ingresar, Cambiar

class Formulario3(forms.ModelForm):
    class Meta:
        model  = Cambiar
        fields = ('contraseña', 'contraseña2')



class Formulario2(forms.ModelForm):
    class Meta:
        model  = Ingresar
        fields = ('usuario', 'contraseña')


class Formulario1(forms.ModelForm):
    class Meta :
        model = Crear
        fields = ('usuario', 'nombre' , 'contraseña' , 'contraseña2' , 'correo' , 'telefono')
