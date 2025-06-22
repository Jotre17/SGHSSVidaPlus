# Importa a classe base AppConfig, usada para configurar o aplicativo no Django
from django.apps import AppConfig

# Define a configuração do app 'profissionais'
class CoreConfig(AppConfig):  
    # Define o tipo de campo automático padrão para chaves primárias
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome do app como ele aparece na estrutura do projeto
    name = 'profissionais'