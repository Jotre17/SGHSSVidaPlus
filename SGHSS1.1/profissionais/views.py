from rest_framework import viewsets
from .models import Profissional, Leito, Internacao
from .serializers import ProfissionalSerializer, LeitoSerializer, InternacaoSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer


class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer
