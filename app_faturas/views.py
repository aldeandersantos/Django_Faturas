from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Compra, Fatura
from .forms import CompraForm

def pagina_inicial(request):
    return render(request, 'app_faturas/index.html')

@login_required
def listar_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    return render(request, 'app_faturas/listar_compras.html', {'compras': compras})

@login_required
def criar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            return redirect('listar_compras')
    else:
        form = CompraForm()
    return render(request, 'app_faturas/criar_compra.html', {'form': form})

@login_required
def listar_faturas(request):
    faturas = Fatura.objects.filter(usuario=request.user)
    return render(request, 'app_faturas/listar_faturas.html', {'faturas': faturas})