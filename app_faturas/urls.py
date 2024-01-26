from django.urls import path
from .views import listar_compras, criar_compra, listar_faturas

urlpatterns = [
    path('listar-compras/', listar_compras, name='listar_compras'),
    path('criar-compra/', criar_compra, name='criar_compra'),
    path('listar-faturas/', listar_faturas, name='listar_faturas'),
    
]