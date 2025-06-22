# Importa o módulo de roteamento (routers) do Django REST Framework.
from rest_framework import routers

# Importa os ViewSets definidos no arquivo views.py.
from .views import ProfissionalViewSet, LeitoViewSet, InternacaoViewSet

# Cria uma instância do DefaultRouter
router = routers.DefaultRouter()

# Registra o ViewSet de Profissional com a rota 'profissionais'.
# Isso cria endpoints como:
router.register(r'profissionais', ProfissionalViewSet)

# Registra o ViewSet de Leito com a rota 'leitos'.
router.register(r'leitos', LeitoViewSet)

# Registra o ViewSet de Internacao com a rota 'internacoes'.
router.register(r'internacoes', InternacaoViewSet)

# Atribui as URLs geradas pelo router à variável urlpatterns.
urlpatterns = router.urls
