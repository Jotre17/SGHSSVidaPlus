# Importa o módulo de roteadores do Django REST Framework
from rest_framework import routers

# Importa o ViewSet que será registrado na URL
from .views import PacienteViewSet

# Cria um roteador padrão do DRF 
router = routers.DefaultRouter()

# Registra o ViewSet no roteador com o prefixo de URL 'pacientes'
router.register(r'pacientes', PacienteViewSet)

# Define as URLs finais como as rotas criadas automaticamente pelo roteador
urlpatterns = router.urls