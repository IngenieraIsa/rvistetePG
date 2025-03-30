from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.TextField(default='https://img.freepik.com/premium-vector/man-avatar-drawing_65141-572.jpg')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
