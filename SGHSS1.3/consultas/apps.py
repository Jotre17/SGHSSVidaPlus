from django.apps import AppConfig 

# Classe de configuração para o app 'consultas'
class ConsultasConfig(AppConfig):
    # Define o tipo padrão de campo de chave primária para os modelos do app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do app conforme está no diretório/projeto
    name = 'consultas'