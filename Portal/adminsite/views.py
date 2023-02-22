from django.shortcuts import render , HttpResponse
from django.contrib import admin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/admin")
def home(request):
    # return HttpResponse("<h1 align=\"center\"> Hello Admin </h1>")
    return render(request, "adminsite/home.html",{})
    
@login_required(login_url="/admin")
def add(request):
    return render(request, "adminsite/add.html",{})
    
@login_required(login_url="/admin")
def update(request):
    return render(request, "adminsite/update.html",{})
    
@login_required(login_url="/admin")
def delete(request):
    return render(request, "adminsite/delete.html",{})
    
@login_required(login_url="/admin")
def attendance(request):
    return render(request, "adminsite/attendance.html",{})

@login_required(login_url="/admin")    
def leave(request):
    # return HttpResponse("<h1 align=\"center\"> Hello Admin </h1>")
    return render(request, "adminsite/leaverecord.html",{})
    