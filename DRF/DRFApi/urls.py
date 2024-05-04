from django.urls import path
from . import views

urlpatterns = [
    path('notes/', view=views.getNotes,name="notes"),
    path('notes/<pk>', view=views.getNote,name="note"),
    path('notes/createnote', view=views.createNote,name="note"),
]