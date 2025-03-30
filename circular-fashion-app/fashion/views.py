from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            try:
                # Busca al usuario en la base de datos
                usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
                # Simula una sesión (puedes usar Django's auth más adelante)
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                messages.success(request, f"¡Bienvenido, {usuario.nombre}!")
                return redirect('inicio')  # Redirige a la URL con el nombre 'inicio'
            except Usuario.DoesNotExist:
                messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
    else:
        form = LoginForm()
    return render(request, 'fashion/login.html', {'form': form})

def inicio(request):
    return render(request, 'fashion/inicio.html')  # Asegúrate de tener una plantilla llamada inicio.html