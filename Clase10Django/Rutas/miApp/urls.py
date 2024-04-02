
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_usuarios),
    #path('create/', views.crear_usuario), 
    path('create/<str:nombre>/<str:apellido>/<int:edad>', views.crear_usuario), # Sección crear user por url
    path('filter/<int:edad>', views.filtrar_usuarios_edad),
    path('update/<int:id>', views.update_usuario_id),
    path('deleteall/', views.delete_todos_usuarios),
    path('delete/<int:id>', views.delete_usuario_id),
    path('jason1', views.ejemplo_jason_view1),
    path('jason2', views.ejemplo_jason_views2)
    
    
    
]

