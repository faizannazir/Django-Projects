from django.shortcuts import render
from . import forms
from .models import Books

# Create your views here.
def index(request):
    books = Books.objects.all()
    context = {"books":books}
    return render(request,template_name="api/index.html", context=context)

def book(request,bookId):
    return render(request,template_name="api/detail.html")
