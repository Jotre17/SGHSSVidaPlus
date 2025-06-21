# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

## Descrição
O SGHSS é um sistema de gestão hospitalar e de serviços de saúde desenvolvido para a instituição VidaPlus, que administra hospitais, clínicas de bairro, laboratórios e equipes de home care.

## Requisitos
- Python 3.8+
- Django 4.2+
- Django REST Framework
- Outras dependências listadas em requirements.txt

## Instalação

1. Clone o repositório:
```
git clone <url-do-repositorio>
cd SGHSS
```

2. Crie e ative um ambiente virtual:
```
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Configure o banco de dados no arquivo settings.py:
```python
# Para SQLite (padrão)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

Para MySQL (descomente e configure)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sghss',
        'USER': 'root',
        'PASSWORD': '---',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Execute as migrações:
```
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário:
```
python manage.py createsuperuser
```

7. Inicie o servidor:
```
python manage.py runserver
```

## Estrutura do Projeto

O projeto está organizado em 5 aplicações principais:

1. **core**: Contém funcionalidades centrais como unidades de saúde e registro de acessos
2. **pacientes**: Gerenciamento de pacientes e histórico médico
3. **profissionais**: Gerenciamento de profissionais de saúde.
4. **consultas**: Agendamento e gerenciamento de consultas e prontuários
5. **administracao**: Configurações do sistema, relatórios e administração
