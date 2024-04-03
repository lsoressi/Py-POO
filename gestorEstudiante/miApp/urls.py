from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:nombre>/<str:apellido>/<int:edad>/<int:nota>', views.crear_Estudiante), # Sección crear estudiante
    path('', views.mostrar_Estudiantes),
    path('filtro/<int:edad>', views.filtrar_estudiante_edad),
    path('actualizarnota/<int:id>', views.actualizar_nota_id),
    path('eliminar/<int:id>', views.eliminar_estudiante_id)

]