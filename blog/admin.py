from django.contrib import admin
from .models import Cambiar, Ingresar, Crear
# Register your models here.

admin.site.register(Crear)
admin.site.register(Ingresar)
admin.site.register(Cambiar)