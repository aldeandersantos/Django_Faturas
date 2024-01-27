from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView as DjangoLogoutView
from django.http import HttpResponseNotAllowed
from django.contrib.auth import login as logout

class CustomLoginView(LoginView):
    template_name = 'app_login/login.html'

class CustomLogoutView(DjangoLogoutView):
    template_name = 'app_login/logout.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')
