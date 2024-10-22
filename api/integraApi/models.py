from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Coin(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_balance(self, amount):
        self.balance += amount
        self.save()

    @staticmethod
    def get_current_balance():
        coin, created = Coin.objects.get_or_create(id=1) 
        return coin

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        coin = Coin.get_current_balance()
        coin.update_balance(self.amount)

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        coin = Coin.get_current_balance()
        coin.update_balance(-self.amount)
