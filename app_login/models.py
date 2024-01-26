from django.db import models
from app_faturas.models import Cliente as FaturasCliente

class Cliente(models.Model):
    faturas_cliente = models.OneToOneField(FaturasCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.faturas_cliente.user.username
