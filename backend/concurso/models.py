from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import uuid

# Se usará un modelo de usuario personalizado para flexibilidad
class Participante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # Validación para evitar registros duplicados [cite: 29]
    telefono = models.CharField(max_length=20)
    
    # Campos de control del flujo
    password = models.CharField(max_length=128, null=True, blank=True) # Se establecerá en la activación [cite: 32]
    verificado = models.BooleanField(default=False) # Estado de verificación de correo [cite: 49]
    token_verificacion = models.UUIDField(default=uuid.uuid4)
    es_participante = models.BooleanField(default=False) # Indica si la cuenta está activa [cite: 32, 33]
    es_ganador = models.BooleanField(default=False)
    
    fecha_inscripcion = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
    
    def __str__(self):
        return self.email

# ... (Posteriormente se añadirán migraciones)