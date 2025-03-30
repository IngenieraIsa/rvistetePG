from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from fashion import views

urlpatterns = [
    path('', lambda request: redirect('login/')),  # Redirige la raíz al login
    path('login/', views.login_view, name='login'),  # Ruta para el login
    path('inicio/', views.inicio, name='inicio'),  # Ruta para la página de inicio
]