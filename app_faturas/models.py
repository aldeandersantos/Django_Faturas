from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Compra(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now, editable=True)

    ano = models.IntegerField(default=timezone.now().year, editable=True)
    mes = models.IntegerField(default=timezone.now().month, editable=True)

    def __str__(self):
        return f'{self.usuario.username} | {self.nome}'
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
