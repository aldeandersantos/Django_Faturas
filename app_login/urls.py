from django.urls import path
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]