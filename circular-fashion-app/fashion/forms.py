# filepath: fashion/forms.py
from django import forms

class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo electrónico", max_length=150, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'
    }))
    contrasena = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))