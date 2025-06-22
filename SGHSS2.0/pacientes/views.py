# Importa o módulo de viewsets do Django REST Framework
from rest_framework import viewsets

# Importa o modelo Paciente definido em models.py
from .models import Paciente

# Importa o serializer correspondente ao modelo Paciente
from .serializers import PacienteSerializer

# Define a view baseada em ModelViewSet 
class PacienteViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados a ser usado nas requisições 
    queryset = Paciente.objects.all()

    # Define o serializer que converte objetos Paciente <-> JSON
    serializer_class = PacienteSerializer


