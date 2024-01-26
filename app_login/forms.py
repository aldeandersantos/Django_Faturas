from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Se você precisar adicionar campos adicionais ao formulário, faça isso aqui.
    campo_personalizado = forms.CharField(max_length=100, required=True, help_text='Adicione uma descrição aqui.')

    class Meta:
        model = User  # O modelo de usuário padrão do Django
        fields = ('username', 'password1', 'password2')  # Campos padrão do UserCreationForm
