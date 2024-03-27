from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    precio = models.IntegerField()


    def _str_(self):
        return self.nombre
