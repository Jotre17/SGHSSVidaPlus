from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# drf-spectacular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

def home(request):
    return JsonResponse({"mensagem": "API SGHSS esta ativa. Use /admin/ para acessar o painel de administracao."})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # drf-spectacular schema and docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Apps
    path('api/', include('core.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('profissionais.urls')),
    path('api/', include('consultas.urls')),
    path('api/', include('administracao.urls')),
]
