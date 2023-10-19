from django.forms.models import model_to_dict
from django.http import JsonResponse , QueryDict

from .models import Books


def getBook(id):
    book = Books.objects.get(id)
    return JsonResponse(model_to_dict(book))

def getBooks():
    books = Books.objects.all()
    return JsonResponse(model_to_dict(books))

def editBook(request,id):
    request_body = QueryDict(request.body)
    id = request_body.get(id)
    book = Books.objects.get(id)
    return JsonResponse(model_to_dict(book))