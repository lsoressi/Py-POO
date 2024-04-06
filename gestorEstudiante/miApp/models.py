from django.db import models

from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    domicilio = models.CharField(
        max_length = 100,
        blank = True,
        null = True           
            )
    edad = models.IntegerField()
    nota = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido 