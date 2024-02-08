from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Compra(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now, editable=True)
    mes = models.IntegerField(default=timezone.now().month, editable=True)
    ano = models.IntegerField(default=timezone.now().year, editable=True)

    def __str__(self):
        return f'{self.usuario.username} | {self.nome}'

@receiver(post_save, sender=Compra)
def criar_parcelas(sender, instance, **kwargs):
    if instance.parcelas > 1:
        valor_por_parcela = instance.valor / instance.parcelas
        for numero_parcela in range(1, instance.parcelas + 1):
            nome_parcela = f"{instance.nome} {numero_parcela}/{instance.parcelas}"
            nova_compra = Compra(
                nome=nome_parcela,
                valor=valor_por_parcela,
                parcelas=1,  # Cada parcela é tratada como uma compra única
                usuario=instance.usuario,
                data=instance.data,
                mes=instance.mes + numero_parcela - 1,  # Incrementa o mês para cada parcela
                ano=instance.ano
            )
            nova_compra.save()
        instance.delete()
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
