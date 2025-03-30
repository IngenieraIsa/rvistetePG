from django.contrib import admin
from .models import Usuario  # Reemplaza con el nombre correcto del modelo

# Registra el modelo en el panel de administración
admin.site.register(Usuario)