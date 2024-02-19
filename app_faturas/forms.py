from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nome', 'valor', 'parcelas', 'servico_recorrente']