from django.db import models
from django import forms

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=150, unique=True)
    contrasena = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.TextField(default='https://i.pinimg.com/564x/19/b8/d6/19b8d6e9b13eef23ec9c746968bb88b1.jpg')

    class Meta:
        managed = False  # Django no gestionará esta tabla
        db_table = 'usuarios'

    def __str__(self):
        return self.correo

class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo electrónico", max_length=150, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'
    }))
    contrasena = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))