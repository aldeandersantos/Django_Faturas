from django.urls import path
from .views import listar_compras, criar_compra, listar_faturas, pagina_inicial

urlpatterns = [
    path('listar-compras/', listar_compras, name='listar_compras'),
    path('criar-compra/', criar_compra, name='criar_compra'),
    path('listar-faturas/', listar_faturas, name='listar_faturas'),
    path('', pagina_inicial, name='pagina_inicial'),
]