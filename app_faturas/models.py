from django.db import models
from django.contrib.auth.models import User

class Compra(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pessoa = models.CharField(max_length=255)
    parcelas = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Fatura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Outros campos para o cliente, como nome, endereço, etc.

    def __str__(self):
        return self.user.username