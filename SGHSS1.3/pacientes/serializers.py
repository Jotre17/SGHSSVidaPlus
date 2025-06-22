# Importa o módulo de serializers do Django REST Framework
from rest_framework import serializers

# Importa o modelo Paciente para ser serializado
from .models import Paciente

# Define um serializer do tipo ModelSerializer para o modelo Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente             # Define o modelo base do serializer
        fields = '__all__'          # Informa que todos os campos do modelo serão incluídos na serialização