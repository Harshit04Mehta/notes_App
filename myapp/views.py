from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer
from rest_framework.generics import ListAPIView

# Create Notes
class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ListNotesView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Fetch Notes by ID
class FetchNoteView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Query Notes by Title Substring
class QueryNotesByTitleView(APIView):
    def get(self, request):
        title_substring = request.query_params.get('title', '')
        notes = Note.objects.filter(title__icontains=title_substring)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

# Update Note
class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
