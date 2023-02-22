from django.contrib import admin
from django.urls import path
from . views import *

app_name = "adminsite"

urlpatterns = [
    path('', home,name="Home"),
    path('add/', add,name="add"),
    path('update/', update,name="update"),
    path('delete/', delete,name="delete"),
    path('atttendance/', attendance,name="attendance"),
    path('leave/', leave,name="leave"),
    path('logout/', admin.site.login,name="logout"),
]
