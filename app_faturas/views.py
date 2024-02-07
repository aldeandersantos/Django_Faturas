from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Compra
from .forms import CompraForm
from . import service

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
def visualizar_faturas(request, ano=None, mes=None):
    # Lógica para obter a lista de anos com base nas compras existentes
    anos = Compra.objects.filter(usuario=request.user).dates('data', 'year', order='DESC')
    meses = service.nomeMeses()
    selected_mes, selected_ano = service.definirData(request)

    # Lógica para obter as compras do usuário no mês e ano especificados
    compras = Compra.objects.filter(usuario=request.user, ano=selected_ano, mes=selected_mes)

    # Lógica para calcular o total gasto no mês atual
    total_gasto = compras.aggregate(Sum('valor'))['valor__sum']
    
    # Renderizando a página
    return render(request, 'app_faturas/visualizar_faturas.html', {
        'compras': compras,
        'total_gasto': total_gasto,
        'ano': ano,
        'mes': mes,
        'selected_mes': selected_mes,
        'selected_ano': selected_ano,
        'anos': anos,
        'meses': meses,
    })