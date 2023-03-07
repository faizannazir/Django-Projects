from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib import messages

from .models import Reg

from .forms import RegistrationForm

# Create your views here.

def home(request):
    form = RegistrationForm
    return render(request=request,template_name='mysqlapp/index.html',context={'form':form,'user':request.user})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_pass']
        print(email)
        print(password)
        user =auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request,user,backend=Reg)
            return redirect('home')
        else:
            messages.info(request,"Credentials not met ")
            return redirect('login')
    else:
        return render(request, 'mysqlapp/account/signin.html',{})

def register(request):
    if request.method == 'POST':
        username = request.POST['user_first_name'] + request.POST['user_last_name']
        email = request.POST['user_email']
        password = request.POST['user_pass']
        password2 = request.POST['user_con_pass']
        if password == password2:
            if (Reg.objects.filter(email=email).exists()):
                messages.info(request, "Email already exist")
                return redirect('register')
            elif (Reg.objects.filter(email=email).exists()):
                messages.info(request, "Email already exists ")
                return redirect('register')
            else:
                register = Reg.objects.create(name=username,email=email,password=password)
                register.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')
    
    return render(request, 'mysqlapp/account/signup.html',{})