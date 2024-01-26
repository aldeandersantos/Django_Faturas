from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm  # Certifique-se de importar o formulário personalizado

class CustomLoginView(LoginView):
    template_name = 'app_login/login.html'  # Especifique o template para a página de login

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use o formulário personalizado para criação do usuário
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Faça o login automaticamente após o cadastro
            return redirect('listar_faturas')  # Ou para a página desejada
    else:
        form = CustomUserCreationForm()  # Use o formulário personalizado para criação do usuário
    return render(request, 'app_login/cadastrar_cliente.html', {'form': form})
