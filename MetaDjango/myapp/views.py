from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# from django.views.generic import ListView,CreateView,DeleteView,DetailView,RedirectView,UpdateView,DateDetailView
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Home page")


class MyView(View):
    def get(self, request):
        return HttpResponse(f"{request.method} <form method='post'>" +
                        "{% csrf_token %}" +
                        """<input type='submit'>
                        </form>""")

    
    def post(self,request):
        return HttpResponse(f"{request.method}")
