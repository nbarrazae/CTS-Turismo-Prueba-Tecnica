from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Participante
from .serializers import InscripcionSerializer
# from .tasks import enviar_correo_verificacion # Tarea que crearemos con Celery 
# from django.conf import settings # Necesario para generar el enlace de verificación

class InscripcionView(generics.CreateAPIView):
    """
    Endpoint (POST) para la inscripción de nuevos concursantes.
    """
    queryset = Participante.objects.all()
    serializer_class = InscripcionSerializer

    def perform_create(self, serializer):
        participante = serializer.save()
        
        # 1. Guardar la información sin la contraseña
        # La contraseña se establece en el paso de verificación [cite: 32]
        
        # 2. Enviar correo de verificación de manera asíncrona [cite: 31, 56]
        # enviar_correo_verificacion.delay(participante.id) # Reemplazar con la tarea real
        print(f"DEBUG: Tarea asíncrona enviada para verificar a {participante.email} con token {participante.token_verificacion}")
        
        # 3. Respuesta al frontend [cite: 41]
        return Response(
            {"message": "¡Gracias por registrarte! Revisa tu correo para verificar tu cuenta.", "email": participante.email},
            status=status.HTTP_201_CREATED
        )