from django.forms.models import model_to_dict
from django.http import JsonResponse , QueryDict
from django.shortcuts import get_object_or_404
from .models import Books


def getBook(id):
    book = get_object_or_404(Books,id)
    return JsonResponse(model_to_dict(book))

def getBooks():
    books = Books.objects.all()
    return JsonResponse(model_to_dict(books))

def editBook(request,id):
    request_body = QueryDict(request.body)
    id = request_body.get(id)
    book = get_object_or_404(Books,id)
    return JsonResponse(model_to_dict(book))

def deleteBook(request,id):
    book = Books.objects.get(id)
    return JsonResponse(model_to_dict(book.delete))