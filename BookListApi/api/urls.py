from django.urls import path
from .views import *

urlpatterns = [
    path("books/",books,name="books"),
    # path("books/<str:bookId>/",books,name="books"),
    # path("books/<str:bookId>/",editBook,name="books"),
    # path("books/<str:bookId>/",deleteBook,name="books"),
]