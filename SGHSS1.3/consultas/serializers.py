from rest_framework import serializers
from .models import Consulta, Agendamento, Prontuario

# Serializer da model Consulta
# Esse serializer transforma instâncias de Consulta em JSON e vice-versa
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta              # Modelo associado
        fields = '__all__'           # Inclui todos os campos do modelo


# Serializer da model Agendamento
# Usado para serializar dados de agendamentos médicos
class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento          
        fields = '__all__'           


# Serializer da model Prontuario
# Responsável por converter objetos de prontuário em representações JSON
class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario           
        fields = '__all__'           
