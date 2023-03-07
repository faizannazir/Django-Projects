from django.shortcuts import render,redirect
from django.urls import reverse
# Create your views here.

from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})





from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html',context={'user':request.user})



        