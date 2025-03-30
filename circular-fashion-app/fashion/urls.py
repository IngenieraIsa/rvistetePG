from django.contrib import admin
from django.urls import path
from fashion import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para el login
    path('inicio/', views.inicio, name='inicio'),  # Ruta para la página de inicio
]