from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import UserAuthor


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

class UserCreateView(CreateView):
    model = UserAuthor
    template_name = 'userapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('parserapp:index')