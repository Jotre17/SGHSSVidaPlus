import logging
from django.utils import timezone

logger = logging.getLogger('sghss')

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = timezone.now()
        response = self.get_response(request)

        if request.path.startswith('/api/'):
            duration = timezone.now() - start_time
            user = request.user.username if request.user.is_authenticated else 'Anonymous'
            logger.info(
                f"User: {user} | "
                f"Method: {request.method} | "
                f"Path: {request.path} | "
                f"Status: {response.status_code} | "
                f"Duration: {duration.total_seconds():.2f}s"
            )

            if request.user.is_authenticated:
                from core.models import RegistroAcesso
                RegistroAcesso.objects.create(
                    usuario=request.user,
                    acao=f"{request.method} {request.path}",
                    descricao=f"Status: {response.status_code}, Duração: {duration.total_seconds():.2f}s"
                )

        return response