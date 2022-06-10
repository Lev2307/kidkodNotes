from notes.models import NotesModel
from .serializers import NoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.decorators import api_view


class NotesList(generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = NotesModel.objects.all()
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = NotesModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateNote(generics.CreateAPIView):
    serializer_class = NoteSerializer
    queryset = NotesModel.objects.all()

@api_view(['GET', 'DELETE'])
def deleteAllChodenNotesS(request):
    if request.method == 'GET':
        notes = NotesModel.objects.filter(checkbox=True)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    if request.method == 'DELETE':
        notes = NotesModel.objects.filter(checkbox=True)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
