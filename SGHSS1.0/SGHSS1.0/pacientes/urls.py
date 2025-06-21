from rest_framework import routers
from .views import PacienteViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = router.urls
