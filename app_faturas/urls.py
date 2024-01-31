from django.urls import path
from .views import cadastrar_compra, pagina_inicial, visualizar_faturas

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('faturas/', visualizar_faturas, name='visualizar_faturas'),
    path('cadastrar_compra/', cadastrar_compra, name='cadastrar_compra'),
]
