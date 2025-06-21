from rest_framework import serializers
from .models import Consulta, Agendamento, Prontuario

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = '__all__'