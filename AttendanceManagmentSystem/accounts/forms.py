from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','department', 'image', 'contact_no']


# class CustomAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(label="Email:",widget=forms.EmailInput(attrs={'autofocus': True,'type':'email','id':'email'}))
#     password = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
#     )
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         del self.fields['username'] 


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.EmailField(label="Email:", widget=forms.EmailInput(attrs={'autofocus': True, 'type': 'email', 'id': 'email'}))
        self.fields['password'] = forms.CharField(
            label=("Password"),
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        )