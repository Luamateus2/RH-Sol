# RH-SOL

RH-SOL é um sistema de gestão de recursos humanos desenvolvido com Django.

## Estrutura do Projeto

O projeto foi iniciado com:
```sh
django-admin startproject setup
```
E o aplicativo principal foi criado com:
```sh
python manage.py startapp rh
```

A estrutura do projeto é organizada da seguinte forma:
```
setup/
|-- manage.py
|-- setup/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   |-- asgi.py
|
|-- rh/
|   |-- migrations/
|   |-- templates/rh/  # Arquivos de template do app (extensão .htm)
|   |-- static/        # Arquivos estáticos
|   |-- views/
|   |   |-- employee_views.py  # Views relacionadas a funcionários
|   |   |-- user_views.py      # Views relacionadas a usuários
|   |-- models.py  # Definição dos modelos de dados
|   |-- urls.py
|   |-- admin.py
|   |-- tests.py
|
|-- .env  # Variáveis de ambiente (banco de dados, secret key, etc.)
|-- requirements.txt  # Dependências do projeto
```

## Modelos de Dados (models.py)

### UserManager
Gerencia a criação de usuários e superusuários.

### User
Modelo de usuário personalizado baseado em `AbstractBaseUser`.

- `name`: Nome do usuário
- `email`: E-mail (usado como campo de login)
- `is_active`: Define se o usuário está ativo
- `is_staff`: Define se o usuário tem acesso ao admin
- `date_joined`: Data de criação do usuário

### Department
Modelo para departamentos da empresa.

- `name`: Nome do departamento
- `description`: Descrição opcional
- `code`: Código único do departamento
- `creation_date`: Data de criação do departamento
- `status`: Status (Ativo/Inativo)
- `num_employees`: Número de funcionários no departamento

### Employee
Modelo para funcionários.

- `name`: Nome do funcionário
- `cpf`: CPF (único)
- `rg`: RG
- `birth_date`: Data de nascimento
- `ctps`: Número da carteira de trabalho
- `department`: Relacionamento com `Department`

## Configuração do Ambiente

### 1. Clonar o Repositório
```sh
git clone https://github.com/Luamateus2/RH-Sol.git
cd rh-sol
```

### 2. Criar um Ambiente Virtual
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Gerar a Secret Key e Configurar o Arquivo `.env`
Para gerar uma `SECRET_KEY`, execute:
```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Crie um arquivo `.env` na raiz do projeto e adicione:
```
SECRET_KEY=sua_secret_key_gerada
DB_NAME=seubanco
DB_USER=seuusuario
DB_PASSWORD=suasenha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Criar o Banco de Dados
Caso ainda não tenha um banco de dados PostgreSQL configurado, crie um executando:
```sh
psql -U seuusuario -c "CREATE DATABASE seubanco;"
```

### 6. Aplicar Migrações
```sh
python manage.py migrate
```

### 7. Criar um Superusuário (Opcional)
```sh
python manage.py createsuperuser
```

### 8. Executar o Servidor
```sh
python manage.py runserver
```

O sistema estará acessível em `http://127.0.0.1:8000/`

## Tecnologias Utilizadas
- Python
- Django
- PostgreSQL
- HTML, CSS, JavaScript

## Contato
Caso tenha dúvidas ou sugestões, entre em contato através do e-mail: luanakarolineliramateus2021@gmail.com.

---
Desenvolvido por Luana Karoline


