from django.db import models

# Create your models here.
#Models serve para armazenar ou alterar os dados do usuário enviados do aplicativo flutter para o banco

class Funcionario(models.Model):
    class Meta:
        db_table = 'TFPFUN'
        managed = False

    