from django.urls import path
from .views import NotesList, NoteDetail, CreateNote, deleteAllChodenNotesS

urlpatterns = [
    path('notes/', NotesList.as_view(), name="notes"),
    path('notes/<int:pk>/', NoteDetail.as_view(), name="detail_note"),
    path('notes/create/', CreateNote.as_view(), name="create_note"),
    path('notes/delallchosen/', deleteAllChodenNotesS, name="delallchosen"),
]