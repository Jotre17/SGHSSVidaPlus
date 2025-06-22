from rest_framework import routers
# Importa os ViewSets que serão registrados nas rotas
from .views import ConsultaViewSet, AgendamentoViewSet, ProntuarioViewSet

# Cria um roteador padrão do Django REST Framework
# Mapeia automaticamente os métodos HTTP (GET, POST, PUT, DELETE)
# para as ações do ViewSet (list, retrieve, create, update, destroy)
router = routers.DefaultRouter()

# Registra o endpoint '/consultas/' vinculado ao ConsultaViewSet
router.register(r'consultas', ConsultaViewSet)

# Registra o endpoint '/agendamentos/' vinculado ao AgendamentoViewSet
router.register(r'agendamentos', AgendamentoViewSet)

# Registra o endpoint '/prontuarios/' vinculado ao ProntuarioViewSet
router.register(r'prontuarios', ProntuarioViewSet)

# Define as URLs geradas automaticamente pelo roteador
urlpatterns = router.urls

