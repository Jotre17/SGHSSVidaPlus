# Importa a classe base de ViewSets do Django REST Framework
from rest_framework import viewsets

# Importa os modelos que serão manipulados pelas views
from .models import Consulta, Agendamento, Prontuario

# Importa os serializers que transformam os dados dos modelos em JSON e vice-versa
from .serializers import ConsultaSerializer, AgendamentoSerializer, ProntuarioSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados (queryset) que será manipulado por essa view
    queryset = Consulta.objects.all()
    # Define qual serializer será usado para conversão dos dados
    serializer_class = ConsultaSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
