from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Fatura
from .forms import CompraForm

def pagina_inicial(request):
    return render(request, 'app_faturas/index.html')

@login_required
def cadastrar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            return redirect('visualizar_faturas')
    else:
        form = CompraForm()
    return render(request, 'app_faturas/cadastrar_compra.html', {'form': form})

@login_required
def visualizar_faturas(request):
    faturas = Fatura.objects.filter(usuario=request.user)
    return render(request, 'app_faturas/visualizar_faturas.html', {'faturas': faturas})
