from django.urls import path
from userapp import views
from django.contrib.auth.views import LogoutView
from .views import UserCreateView
app_name = 'userapp'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name= 'register'),
    path('profile/<int:pk>/', views.UserDeteil.as_view(), name= 'profile'),
    path('update_token/', views.update_token, name= 'update_token'),
    path('create_token/', views.create_token, name= 'create_token'),
    path('update-token-ajax/', views.update_token_ajax),
]