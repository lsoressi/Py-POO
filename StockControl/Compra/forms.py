from django import forms
from .models import Proveedor
from .models import Producto

class proveedor_Formulario(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'
        #fields = ['rSocial', 'domicilio', 'cuit']

class producto_Formulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
       

