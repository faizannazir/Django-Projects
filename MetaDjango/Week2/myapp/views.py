from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
# from django.views.generic import ListView,CreateView,DeleteView,DetailView,RedirectView,UpdateView,DateDetailView
# Create your views here.

def home(request):
    # {% url \'myapp:Class\' %}
    return HttpResponse(f"Welcome to Home page <br> {reverse('myapp:Class')} ")
class Home(View):
    def get(self,request):
        return HttpResponse(f"This is randered with classBased view <br> {reverse('myapp:home')}")
