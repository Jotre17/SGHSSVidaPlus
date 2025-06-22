from rest_framework import viewsets
from .models import Consulta, Agendamento, Prontuario
from .serializers import ConsultaSerializer, AgendamentoSerializer,ProntuarioSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
