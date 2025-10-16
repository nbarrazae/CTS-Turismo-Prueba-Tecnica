from rest_framework import serializers
from .models import Participante

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['nombre_completo', 'email', 'telefono']
        extra_kwargs = {'email': {'validators': []}} # Remover el validador por defecto, usaremos un método en la vista

    # Validación personalizada (más clara y controlada)
    def validate_email(self, value):
        if Participante.objects.filter(email=value).exists():
            # El sistema no permite un registro duplicado [cite: 29, 40]
            raise serializers.ValidationError("Este correo ya se encuentra inscrito.") 
        return value    