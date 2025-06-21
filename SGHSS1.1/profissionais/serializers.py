from rest_framework import serializers
from .models import Profissional, Leito, Internacao

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'


class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'


class InternacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internacao
        fields = '__all__'

