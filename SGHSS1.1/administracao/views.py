from rest_framework import viewsets
from .models import RegistroAcesso, Suprimento, RelatorioFinanceiro
from core.models import Administrador
from .serializers import (
    AdministradorSerializer, RegistroAcessoSerializer,
    suprimentoSerializer, RelatorioFinanceiroSerializer
)


class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer


class RegistroAcessoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcesso.objects.all()
    serializer_class = RegistroAcessoSerializer


class suprimentoViewSet(viewsets.ModelViewSet):
    queryset = Suprimento.objects.all()
    serializer_class = suprimentoSerializer


class RelatorioFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = RelatorioFinanceiro.objects.all()
    serializer_class = RelatorioFinanceiroSerializer
