from rest_framework import serializers
from notes.models import NotesModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ['header', 'body', 'status', 'date', 'checkbox', 'image']