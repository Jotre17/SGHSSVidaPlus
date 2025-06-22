from rest_framework import viewsets, filters
from .models import UnidadeSaude
from .serializers import UnidadeSaudeSerializer


class UnidadeSaudeViewSet(viewsets.ModelViewSet):
    
    # Define o queryset base para todas as operações
    queryset = UnidadeSaude.objects.all()
    
    # Define o serializer que será usado para transformar o modelo em JSON e vice-versa
    serializer_class = UnidadeSaudeSerializer

    # Adiciona funcionalidades extras de filtro, ordenação e busca
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    # Permite buscas por nome, cidade e tipo da unidade de saúde usando ?search=
    search_fields = ['nome', 'cidade', 'tipo']

    # Permite ordenação por nome ou cidade com ?ordering=nome ou ?ordering=-cidade
    ordering_fields = ['nome', 'cidade']