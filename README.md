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
|   |-- models.py
|   |-- urls.py
|   |-- admin.py
|   |-- tests.py
|
|-- .env  # Variáveis de ambiente (banco de dados, secret key, etc.)
|-- requirements.txt  # Dependências do projeto
```

## Configuração do Ambiente

### 1. Clonar o Repositório
```sh
git clone <URL_DO_REPOSITORIO>
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

### 4. Configurar o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione:
```
SECRET_KEY=suachavesecreta
DB_NAME=seubanco
DB_USER=seuusuario
DB_PASSWORD=suasenha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Aplicar Migrações
```sh
python manage.py migrate
```

### 6. Criar um Superusuário (Opcional)
```sh
python manage.py createsuperuser
```

### 7. Executar o Servidor
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
Caso tenha dúvidas ou sugestões, entre em contato.

---
Desenvolvido por [Seu Nome]

