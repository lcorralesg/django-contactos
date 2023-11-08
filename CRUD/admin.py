from django.contrib import admin

# Register your models here.

from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'direccion')

