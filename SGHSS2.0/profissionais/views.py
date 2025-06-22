# Importa o módulo 'viewsets' do DRF.
from rest_framework import viewsets

# Importa os modelos que serão utilizados nas views.
from .models import Profissional, Leito, Internacao

# Importa os serializers correspondentes aos modelos.
from .serializers import ProfissionalSerializer, LeitoSerializer, InternacaoSerializer

# Define um ViewSet para o modelo Profissional.
class ProfissionalViewSet(viewsets.ModelViewSet):
    # Define o queryset padrão, ou seja, o conjunto de objetos retornados pelas requisições.
    queryset = Profissional.objects.all()
    # Define o serializer que será usado para converter os dados dos objetos.
    serializer_class = ProfissionalSerializer


# Define um ViewSet para o modelo Leito.
class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer


# Define um ViewSet para o modelo Internacao.
class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer