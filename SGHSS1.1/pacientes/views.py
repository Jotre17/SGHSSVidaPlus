from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer
from core.permissoes import IsAdministradorTotal, IsReadOnly

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdministradorTotal()]
        return [IsReadOnly()]