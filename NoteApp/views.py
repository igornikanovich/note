from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Category, Note


class CategoryListView(generic.ListView):
    categoryList = Category.objects.all()
    template_name = 'index.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', ]

    def get_success_url(self):
        return reverse('index')


class NoteListView(generic.ListView):
    noteList = Note.objects.all()
    template_name = 'noteapp/note_list.html'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text', ]

    def get_success_url(self):
        return reverse('note-list')
