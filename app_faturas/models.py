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

