from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from .models import UserAuthor
from django.http import JsonResponse, HttpResponseRedirect


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

class UserCreateView(CreateView):
    model = UserAuthor
    template_name = 'userapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('parserapp:index')
class UserDeteil(DetailView):
    template_name = 'userapp/profile.html'
    model = UserAuthor
def update_token(request):
    request.user.auth_token.delete()
    token = Token.objects.create(user=request.user)
    return HttpResponseRedirect(reverse_lazy('userapp:profile', kwargs={'pk': request.user.pk}))

def create_token(request):
    token = Token.objects.create(user=request.user)
    return HttpResponseRedirect(reverse_lazy('userapp:profile', kwargs={'pk': request.user.pk}))
def update_token_ajax(request):

    request.user.auth_token.delete()
    token = Token.objects.create(user=request.user)
    return JsonResponse({'key': token.key})
def create_token_ajax(request):
    token = Token.objects.create(user=request.user)
    return JsonResponse({'key': token.key})
