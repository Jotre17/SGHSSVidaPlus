# Importa o módulo 'os', que permite configurar variáveis de ambiente.
import os

# Importa a função 'get_wsgi_application' do Django,
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente que informa ao Django qual é o arquivo de configurações.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGHSS.settings')

# Cria e expõe a aplicação WSGI.
application = get_wsgi_application()

