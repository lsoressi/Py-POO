from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 100)
    edad = models.IntegerField()


    def _str_(self):
        return self.nombre