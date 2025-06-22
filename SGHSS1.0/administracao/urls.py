# app: administracao
# script: urls.py

from rest_framework import routers
from .views import (
    AdministradorViewSet, RegistroAcessoViewSet,
    suprimentoViewSet, RelatorioFinanceiroViewSet
)

router = routers.DefaultRouter()
router.register(r'administradores', AdministradorViewSet)
router.register(r'registros-acesso', RegistroAcessoViewSet)
router.register(r'suprimento', suprimentoViewSet)
router.register(r'relatorios-financeiros', RelatorioFinanceiroViewSet)

urlpatterns = router.urls
