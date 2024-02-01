from django.urls import path
from .views import (
    pagina_inicial,
    cadastrar_compra,
    visualizar_faturas,
)

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('cadastrar_compra/', cadastrar_compra, name='cadastrar_compra'),
    path('faturas/', visualizar_faturas, name='visualizar_faturas'),
]
