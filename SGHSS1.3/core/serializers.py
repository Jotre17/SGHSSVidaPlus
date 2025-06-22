# Importa a base de serialização do Django REST Framework
from rest_framework import serializers

# Importa o modelo que será serializado
from .models import UnidadeSaude

class UnidadeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeSaude        # Define o modelo que este serializer representa
        fields = '__all__'          # Inclui todos os campos do modelo automaticamente