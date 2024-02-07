from datetime import datetime

def nomeMeses():
    # Lógica para obter a lista de meses
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
    return meses

def definirData(request, ano=None, mes=None):
    if request.method == 'POST':
        selected_ano = int(request.POST.get('ano', datetime.now().year))
        selected_mes = int(request.POST.get('mes', datetime.now().month))
    else:
        selected_ano = ano if ano else datetime.now().year
        selected_mes = mes if mes else datetime.now().month

    return (selected_mes, selected_ano)