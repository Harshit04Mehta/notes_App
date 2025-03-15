from django.urls import path, include
# from .views import CreateNoteView, FetchNoteView, QueryNotesByTitleView, UpdateNoteView, ListNotesView
from .views import *

urlpatterns = [
    path('notes/', CreateNoteView.as_view(), name='create-note'),
    path('notes/<int:pk>/', FetchNoteView.as_view(), name='fetch-note'),
    path('notes/query/', QueryNotesByTitleView.as_view(), name='query-notes-by-title'),
    path('notes/update/<int:pk>/', UpdateNoteView.as_view(), name='update-note'),
    path('notes/all/', ListNotesView.as_view(), name='list-notes'),
]