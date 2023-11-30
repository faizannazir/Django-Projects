from django.shortcuts import render
from .forms import *
from .models import Books
from django.forms.models import model_to_dict
from django.http import JsonResponse , QueryDict
from django.shortcuts import get_list_or_404,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


# Create your views here.
# def index(request):
#     books = Books.objects.all()
#     book_list = []
#     for book in books:
#         book_dict = model_to_dict(book)
#         book_list.append(book_dict)
#     return JsonResponse(book_list,safe=False)
#    # context = {"books":books}
#     # return render(request,template_name="api/index.html", context=context)

# def book(request,bookId):
#     book = Books.objects.get(bookId)
#     return JsonResponse(model_to_dict(book),safe=False)
#     # return render(request,template_name="api/detail.html")

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Books.objects.all().values()
        return JsonResponse({'books':list(books)})
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('title')
        price = request.POST.get('title')
        book = Books(title = title, author = author, price = price)
        try:
            book.save()
        except IntegrityError():
            return JsonResponse({'error':'true' , 'message' : 'required field missing' }, status = 400)
        
        return JsonResponse(model_to_dict(book),status=201)