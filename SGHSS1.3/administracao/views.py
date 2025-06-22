# Importações necessárias do Django REST Framework
from rest_framework import viewsets

# Importa os modelos que serão manipulados pelas views
from .models import RegistroAcesso, Suprimento, RelatorioFinanceiro
from core.models import Administrador

# Importa os serializers responsáveis por transformar os modelos em JSON e vice-versa
from .serializers import (
    AdministradorSerializer, RegistroAcessoSerializer,
    suprimentoSerializer, RelatorioFinanceiroSerializer
)


# ViewSet para o modelo Administrador
# Permite listagem, criação, atualização e remoção de administradores
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()  # Consulta todos os registros do modelo
    serializer_class = AdministradorSerializer  # Define qual serializer será usado


# ViewSet para o modelo RegistroAcesso
# Permite operações CRUD sobre os registros de acesso dos administradores
class RegistroAcessoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcesso.objects.all()
    serializer_class = RegistroAcessoSerializer


# ViewSet para o modelo Suprimento
# Gerencia os suprimentos das unidades de saúde
class suprimentoViewSet(viewsets.ModelViewSet):
    queryset = Suprimento.objects.all()
    serializer_class = suprimentoSerializer


# ViewSet para o modelo RelatorioFinanceiro
# Gerencia registros financeiros das unidades
class RelatorioFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = RelatorioFinanceiro.objects.all()
    serializer_class = RelatorioFinanceiroSerializer
