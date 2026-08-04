from django.urls import path

from .views import *

urlpatterns = [
    path('notes/', NoteView.as_view(), name='note_view'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('notes/new/', NoteCreateView.as_view(), name='note_new'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name='note_delete')
]
