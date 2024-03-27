
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auriculares/', include('MiApp.urls')),
    path('mascota/', include('crearMascota.urls')),
]
