from rest_framework import serializers
from .models import Administrador, RegistroAcesso, Suprimento, RelatorioFinanceiro

# Serializer para o modelo Administrador.
# Permite converter instâncias do modelo Administrador para JSON e vice-versa.
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador         # Modelo base usado pelo serializer
        fields = '__all__'           # Inclui todos os campos do modelo no serializer


# Serializer para o modelo RegistroAcesso.
# Responsável por representar logs de acesso feitos por administradores.
class RegistroAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcesso
        fields = '__all__'


# Serializer para o modelo Suprimento.
# Usado para manipular dados de itens armazenados em unidades de saúde.
class suprimentoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Suprimento
        fields = '__all__'


# Serializer para o modelo RelatorioFinanceiro.
# Utilizado para gerenciar a entrada e saída de dados financeiros das unidades.
class RelatorioFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioFinanceiro
        fields = '__all__'