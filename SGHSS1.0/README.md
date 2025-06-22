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

## API Endpoints

### Autenticação
- POST /api/token/ - Obter token JWT
- POST /api/token/refresh/ - Atualizar token JWT

### Core
- GET /api/ - API root
- GET/POST /api/unidades/ - Listar/criar unidades de saúde
- GET /api/registros/ - Listar registros de acesso (admin only)

### Pacientes
- GET/POST /api/pacientes/ - Listar/criar pacientes
- GET/PUT/DELETE /api/pacientes/{id}/ - Detalhes/atualizar/excluir paciente
- GET /api/pacientes/{id}/prontuario/ - Obter histórico médico
- PUT /api/pacientes/{id}/atualizar_prontuario/ - Atualizar histórico médico
- GET /api/pacientes/buscar/?termo={termo} - Buscar pacientes

### Profissionais
- GET/POST /api/profissionais/ - Listar/criar profissionais
- GET/PUT/DELETE /api/profissionais/{id}/ - Detalhes/atualizar/excluir profissional
- GET /api/profissionais/{id}/agenda/ - Obter agenda do profissional
- GET /api/profissionais/buscar/?termo={termo} - Buscar profissionais
- GET/POST /api/agendas/ - Listar/criar agendas
- GET /api/agendas/disponiveis/ - Listar horários disponíveis

## Segurança

O sistema implementa as seguintes medidas de segurança:

1. Autenticação JWT (JSON Web Token)
2. Controle de acesso baseado em permissões
3. Registro de logs de acesso
4. Criptografia de dados sensíveis
5. Conformidade com a LGPD

## Testes
O projeto conta com um script de testes automatizados para validação das funcionalidades principais do sistema SGHSS. Os testes simulam operações reais de uso da API REST.

As ações testadas incluem:

1. Autenticação JWT: Valida a obtenção de token com credenciais válidas.

2. Cadastro de unidade de saúde: Garante que uma nova unidade pode ser registrada com sucesso.

3. Criação de profissional de saúde: Simula o vínculo com uma unidade e o registro completo do profissional.

4. Cadastro de paciente: Testa o registro de dados pessoais e de contato.

5. Agendamento de consulta: Verifica o relacionamento entre paciente, profissional e data/hora da consulta.