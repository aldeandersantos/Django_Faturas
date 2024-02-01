from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Compra
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
def visualizar_faturas(request, ano=None, mes=None):
    # Obtendo a lista de anos com base nas compras existentes
    anos = Compra.objects.filter(usuario=request.user).dates('data', 'year', order='DESC')
    
    # Obtendo a lista de meses
    meses = [
        {'numero': 1, 'nome': 'Janeiro'},
        {'numero': 2, 'nome': 'Fevereiro'},
        {'numero': 3, 'nome': 'Março'},
        {'numero': 4, 'nome': 'Abril'},
        {'numero': 5, 'nome': 'Maio'},
        {'numero': 6, 'nome': 'Junho'},
        {'numero': 7, 'nome': 'Julho'},
        {'numero': 8, 'nome': 'Agosto'},
        {'numero': 9, 'nome': 'Setembro'},
        {'numero': 10, 'nome': 'Outubro'},
        {'numero': 11, 'nome': 'Novembro'},
        {'numero': 12, 'nome': 'Dezembro'},
    ]

    if not ano or not mes:
        # Se ano ou mês não forem fornecidos, assume o ano e mês atuais
        ano = datetime.now().year
        mes = datetime.now().month

    # Convertendo ano e mes para inteiros
    ano = int(ano)
    mes = int(mes)

    # Filtra as compras do usuário logado no ano e mês fornecidos
    compras = Compra.objects.filter(usuario=request.user, data__year=ano, data__month=mes)

    # Calcula o total gasto no ano e mês fornecidos
    total_gasto = compras.aggregate(Sum('valor'))['valor__sum']

    return render(request, 'app_faturas/visualizar_faturas.html', {
        'compras': compras,
        'total_gasto': total_gasto,
        'ano': ano,
        'mes': mes,
        'anos': anos,
        'meses': meses,
    })
