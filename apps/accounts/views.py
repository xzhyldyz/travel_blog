from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView,FormView
from .forms import RegisterForm,LoginForm
from .models import User
# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'pages/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = authenticate(username=username, password=password, email=email)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Пользователь забанен')
        else:
            return HttpResponse('Неправильный логин или пароль или такого юзера нет')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')


