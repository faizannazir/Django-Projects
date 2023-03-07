from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CreateUser(UserCreationForm):
    id = forms.IntegerField()
    firstname = forms.CharField(max_length=12)
    lastname = forms.CharField(max_length=12)
    image = forms.ImageField()
    department = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['firstname','lastname','email','image','password1','password2']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email','department', 'image', 'contact_no']







from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email:",widget=forms.EmailInput(attrs={'autofocus': True,'type':'email','name':'email','id':'email'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )




