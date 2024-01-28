from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Fatura, Compra
from .forms import CompraForm

def pagina_inicial(request):
    return render(request, 'app_faturas/index.html')

@login_required
def cadastrar_compra(request):
    compras = Compra.objects.filter(usuario=request.user)
    form = CompraForm(request.POST or None, initial={'usuario': request.user})

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if 'add_another' in request.POST:
                # Redireciona para a página de cadastro novamente
                return redirect('cadastrar_compra')
            elif 'go_to_home' in request.POST:
                # Redireciona para a página inicial
                return redirect('pagina_inicial')

    return render(request, 'app_faturas/cadastrar_compra.html', {'compras': compras, 'form': form})

@login_required
def visualizar_faturas(request):
    faturas = Fatura.objects.filter(usuario=request.user)
    return render(request, 'app_faturas/visualizar_faturas.html', {'faturas': faturas})
