from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import LoginSerializer, UsuarioSerializer

# Create your views here.

def login_view(request):
    return render(request, 'usuarios/login.html')

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            correo = serializer.validated_data['correo']
            contrasena = serializer.validated_data['contrasena']
            try:
                usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
                usuario_serializer = UsuarioSerializer(usuario)
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
