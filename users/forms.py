from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):  # форма регистрации
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomAuthenticationForm(AuthenticationForm):  # форма аутентификации
    class Meta:
        model = User
        fields = ('username', 'password')
