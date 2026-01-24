from django.contrib.auth.forms import UserCreationForm
from .models import UserAuthor
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserAuthor
        fields = ['username', 'email', 'password1', 'password2']