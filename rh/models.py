from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O campo email é obrigatório')
        if not nome:
            raise ValueError('O campo nome é obrigatório')

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(email, nome, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='usuario_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_user_permissions')

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)  
    codigo = models.CharField(max_length=20, unique=True, blank=False, null=False) 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(
        max_length=20, 
        choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], 
        default='Ativo'
    )  
    num_funcionarios = models.IntegerField(default=0)
    def __str__(self):
        return self.nome
    

class Funcionario(models.Model):
    nome = models.CharField(max_length=400)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    rg = models.CharField(max_length=20, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    ctps = models.CharField(max_length=20, blank=False, null=False)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT) 
    
    def __str__(self):
        return self.nome 