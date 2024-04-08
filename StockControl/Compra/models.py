from django.db import models

# Create your models here.
class Proveedor(models.Model):
    rSocial = models.CharField(max_length = 100)
    domicilio = models.CharField(max_length = 100)
    cuit = models.IntegerField()

    def _str_(self):
        return self.rSocial
    

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    precio = models.IntegerField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre


    
   