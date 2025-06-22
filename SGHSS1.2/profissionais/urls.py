from rest_framework import routers
from .views import ProfissionalViewSet, LeitoViewSet, InternacaoViewSet

router = routers.DefaultRouter()
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'leitos', LeitoViewSet)
router.register(r'internacoes', InternacaoViewSet)

urlpatterns = router.urls
