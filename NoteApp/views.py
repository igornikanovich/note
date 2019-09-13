from sqlite3 import IntegrityError

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, NoReverseMatch

from .utils import crypt
from .models import Category, Note
from .forms import TitleNoteForm, NoteForm
from Note.settings import CRYPT_PASSWORD


class CategoryListView(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        new_category = request.POST['addnewcat']
        if len(new_category) > 0:
            try:
                category = Category.objects.create(name=new_category)
                category.save()
                return redirect('index')
            except:
                return redirect('index')
        else:
            return redirect('index')

# class CategoryCreateView(CreateView):
#     # model = Category
#     # fields = ['name', ]
#     template_name = 'index.html'


# class CategoryDetailView(generic.DetailView):
#     model = Category
#     template_name = 'noteapp/category_detail.html'


# class NoteListView(generic.ListView):
#     queryset = Note.objects.all()
#     template_name = 'noteapp/note_list.html'


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
            return redirect('index')
    else:
        form = TitleNoteForm()
    return render(request, 'noteapp/note_form.html', {'form': form})


class NoteTextUpdateView(UpdateView):

    def get(self, request, *args, **kwargs):
        note = Note.objects.get(slug=self.kwargs['slug'])
        form = NoteForm(initial={'title': note.title, 'text': note.text})
        return render(request, "noteapp/note_detail.html", {'form': form, 'title': note.title})

    def post(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, slug=kwargs['slug'])
        form = NoteForm(request.POST)
        passw = request.POST['password']
        if form.is_valid() and passw == CRYPT_PASSWORD:
            notetext = form.cleaned_data['text']
            notetext = crypt(notetext)
            note.text = notetext
            note.save()
            return HttpResponseRedirect(reverse('note-update', args=[note.slug]))
        return render(request, 'noteapp/note_detail.html', {'form': form, 'title': note.title})
