from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

# Class Based Views 

from .import models 
from django.views import generic

class DogDetailView(generic.DeleteView):
    model  = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'


class ShelterListView(generic.ListView):
    template_name = 'shelter_list.html'
    context_object_name = 'shelters'

    def get_queryset(self):
        return models.Shelter.objects.all()
    

class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name','description' ]