from django.urls import path
from userapp import views
from django.contrib.auth.views import LogoutView
from .views import UserCreateView
app_name = 'userapp'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name= 'register'),
]