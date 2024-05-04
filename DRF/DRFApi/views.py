from django.shortcuts import render
from .Searlizer import NotesSerializer
from .models import Notes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['Get'])
def getNotes(request):
    notes = Notes.objects.all()
    # NotesSerializer.Meta.model = Notes
    # NotesSerializer.Meta.fields = '__all__'
    serializer = NotesSerializer(notes, many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getNote(request,pk):
    note = Notes.objects.get(id=pk)
    serializer = NotesSerializer(note, many = False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def createNote(request):
    print(".......................................")
    print(request.POST)
    if(request.method == "POST"):
        heading  = request.POST.get("heading")
        body  = request.POST.get("body")
        Notes.objects.create(heading=heading,body=body)
        Notes.save()
        return Response("Created",status=status.HTTP_200_OK)
    return Response()
    
