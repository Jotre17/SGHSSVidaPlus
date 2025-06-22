# Importa o módulo 'os', que permite interações com variáveis de ambiente e o sistema operacional.
import os

# Importa a função 'get_asgi_application', 
from django.core.asgi import get_asgi_application

# Define a variável de ambiente 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGHSS.settings')

# Cria a aplicação ASGI. 
application = get_asgi_application()

