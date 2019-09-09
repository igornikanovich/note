from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Category, Note
from .forms import TitleNoteForm, NoteForm


class CategoryListView(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'index.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', ]
    template_name = 'noteapp/category_form.html'

    def get_success_url(self):
        return reverse('index')


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'noteapp/category_detail.html'


class NoteListView(generic.ListView):
    queryset = Note.objects.all()
    template_name = 'noteapp/note_list.html'


class NoteDetailView(generic.DetailView):
    model = Note
    template_name = 'noteapp/note_detail.html'


def add_note_to_notelist(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = TitleNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            note.category = category
            note.save()
            return redirect('category-detail', slug=category.slug)
    else:
        form = TitleNoteForm()
    return render(request, 'noteapp/note_form.html', {'form': form})

def add_textnote_to_note(request, slug):
    # note = get_object_or_404(Note, slug=slug)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            note.save()
            return redirect('note-detail', slug=slug)
    else:
        form = NoteForm()
    return render(request, 'noteapp/note_form.html', {'form': form})
