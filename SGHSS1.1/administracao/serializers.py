from rest_framework import serializers
from .models import Administrador, RegistroAcesso, Suprimento, RelatorioFinanceiro

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'


class RegistroAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcesso
        fields = '__all__'


class suprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suprimento
        fields = '__all__'


class RelatorioFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioFinanceiro
        fields = '__all__'
