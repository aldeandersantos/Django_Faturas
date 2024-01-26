from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faturas/', include('app_faturas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]