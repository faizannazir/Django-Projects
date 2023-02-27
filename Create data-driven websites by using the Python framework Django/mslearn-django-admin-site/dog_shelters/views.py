from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Shelter

# Create your views here.

def index(request):
    return render(request,'dog_shelters/base.html',{})


def shelter_list(request):
    shelters = Shelter.objects.all()
    context = { 'shelters': shelters }
    return render(request, 'dog_shelters/shelter_list.html', context)

def shelter_detail(request, pk):
    shelters = get_object_or_404(Shelter,pk=pk)
    context = { 'shelters': shelters }
    return render(request, 'dog_shelters/shelter_detail.html', context)