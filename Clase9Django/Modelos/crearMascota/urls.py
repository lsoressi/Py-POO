from django.urls import path
from .views import crear_mascota

urlpatterns = [
    path('', crear_mascota, name='crear Mascota')

]