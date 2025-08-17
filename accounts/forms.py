from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# register
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.USER_ROLES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']


# login
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)