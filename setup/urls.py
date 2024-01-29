from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from app_faturas.views import visualizar_faturas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('app_faturas.urls')),
    path('faturas/', visualizar_faturas, name='visualizar_faturas'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('app_login.urls')),
    path('logout/', include('app_login.urls')), 
    path('', RedirectView.as_view(url='inicio/', permanent=False)),  # Redirecionamento para a página inicial
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)