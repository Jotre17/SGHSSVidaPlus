from rest_framework import routers
# Importa os viewsets definidos para o app 'administracao'
from .views import (
    AdministradorViewSet, RegistroAcessoViewSet,
    suprimentoViewSet, RelatorioFinanceiroViewSet
)

# Cria um roteador padrão do DRF 
router = routers.DefaultRouter()

# Registra os endpoints, associando cada ViewSet a uma rota.

# URL: /administradores/ → ligado ao AdministradorViewSet
router.register(r'administradores', AdministradorViewSet)

# URL: /registros-acesso/ → ligado ao RegistroAcessoViewSet
router.register(r'registros-acesso', RegistroAcessoViewSet)

# URL: /suprimento/ → ligado ao suprimentoViewSet
router.register(r'suprimento', suprimentoViewSet)

# URL: /relatorios-financeiros/ → ligado ao RelatorioFinanceiroViewSet
router.register(r'relatorios-financeiros', RelatorioFinanceiroViewSet)

# Define as URLs a partir das rotas geradas automaticamente pelo router
urlpatterns = router.urls
