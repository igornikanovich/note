from django.urls import path

from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='index'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<slug>/create/', views.add_note_to_notelist, name='note-create'),
    path('note/<slug>/update', views.add_textnote_to_note, name='note-update'),
    path('note/<slug>', views.NoteDetailView.as_view(), name='note-detail'),
    # path('note/create/', views.NoteCreateView.as_view(), name='note-create'),
]
