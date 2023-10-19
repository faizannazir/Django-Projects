from django.urls import path
from .views import *

urlpatterns = [
    path("books",index,name="books"),
    path("books/<str:bookId>",book,name="books"),
]