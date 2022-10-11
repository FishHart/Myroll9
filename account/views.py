from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic


'''トップページ'''
class TempView(generic.TemplateView):
    template_name = 'account/base.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

class Logout(LogoutView):
    template_name = 'account/logout_done.html'
