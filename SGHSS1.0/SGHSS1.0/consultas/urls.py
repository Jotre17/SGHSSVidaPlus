from rest_framework import routers
from .views import ConsultaViewSet, AgendamentoViewSet

router = routers.DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = router.urls
