from django.urls import path
from .views import CustomLoginView, cadastrar_cliente

urlpatterns = [
    path('cadastrar-cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('login/', CustomLoginView.as_view(), name='login'),
]