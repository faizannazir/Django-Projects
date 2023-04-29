from django.shortcuts import render

from .forms import ImageForm

# Create your views here.

def image(request):
    form = ImageForm()
    if request.method == 'POST':
        print("POST")
        form = ImageForm(request.POST,request.FILES)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return render(request,'image_db/imageForm.html',context={'form':"Successfull"})
    context={'form': form}
    return render(request,'image_db/imageForm.html',context=context)
