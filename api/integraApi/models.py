from django.db import models

# Create your models here.
#Models serve para armazenar ou alterar os dados do usuário enviados do aplicativo flutter para o banco

class Funcionario(models.Model):
    NOMEFUNC = models.CharField(max_length=20)
    CODFUNC = models.IntegerField(max_length=10)
    CPF = models.InterField(max_length=13)