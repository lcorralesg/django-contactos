from django.db import models

# Create your models here.

# Se manejara una agenda de contactos con sus respectivos campos y CRUD

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=254)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
