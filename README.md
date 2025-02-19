# RH-Sol

#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS=example.com,www.example.com
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ENV DEBUG=True
CSRF (Cross-Site Request Forgery)

Em produção, é importante garantir que você tenha uma configuração segura de CSRF:

python
Copiar
CSRF_COOKIE_SECURE = True