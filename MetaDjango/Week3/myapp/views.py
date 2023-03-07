from django.shortcuts import render

from . import forms


# Create your views here.

def home(request):
    # form = forms.NameForm
    form = forms.DemoForm
    return render(request, 'myapp/home.html', {'form': form})


def signup(request):
    # form = forms.NameForm
    form = forms.SignupForm
    return render(request, 'myapp/home.html', {'form': form})