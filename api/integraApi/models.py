from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Coin(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def atualizar_saldo(self, valor):
        self.saldo += valor
        self.save()

    @staticmethod
    def get_saldo_atual():
        coin, created = Coin.objects.get_or_create(id=1)  # Assume apenas uma instância
        return coin

class Entrada(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        coin = Coin.get_saldo_atual()
        coin.atualizar_saldo(self.valor)

class Saída(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        coin = Coin.get_saldo_atual()
        coin.atualizar_saldo(-self.valor)
