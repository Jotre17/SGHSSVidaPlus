# Importa o módulo 'serializers' do Django REST Framework,
from rest_framework import serializers
# Importa os modelos que serão serializados.
from .models import Profissional, Leito, Internacao

# Define um serializer para o modelo Profissional.
class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo associado a este serializer.
        model = Profissional
        fields = '__all__'


# Define um serializer para o modelo Leito.
class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'


# Define um serializer para o modelo Internacao.
class InternacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internacao
        fields = '__all__'

