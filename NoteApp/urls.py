from django.urls import path

from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='index'),
    path('category/<slug>/create/', views.AddTitleNoteView.as_view(), name='Note-create'),
    path('Note/<slug>/update', views.NoteTextUpdateView.as_view(), name='Note-update'),
]
