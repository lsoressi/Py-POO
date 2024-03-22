from django.urls import path
from MiAppHolaMundo import views

urlpatterns = [
    path('saludo/', views.saludar),
    path('despedida/', views.despedida),
]

