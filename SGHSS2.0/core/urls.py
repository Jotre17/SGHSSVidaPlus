# Importações padrão do Django e DRF para rotas
from django.urls import path
from rest_framework import routers

# Importa as views padrão de obtenção e renovação de tokens JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Importa o ViewSet que será registrado nas rotas da API
from .views import UnidadeSaudeViewSet

router = routers.DefaultRouter()
router.register(r'unidades', UnidadeSaudeViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Inclusão das rotas geradas pelo router ao urlpatterns
urlpatterns += router.urls