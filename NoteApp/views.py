from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .utils import crypt
from .models import Category, Note
from .forms import TitleNoteForm, NoteForm
from Note.settings import CRYPT_PASSWORD


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
            return redirect('index')
    else:
        form = TitleNoteForm()
    return render(request, 'noteapp/note_form.html', {'form': form})



class NoteTextUpdateView(UpdateView):
    model = Note
    fields = ['text', ]
    template_name = 'noteapp/note_form.html'


    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        note = Note.objects.get(slug=slug)
        title = note.title
        text = note.text
        form = NoteForm(initial={'title': title, 'text': text})
        context = {'form': form}
        return render(request, "noteapp/note_form.html", context)


    def post(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, slug=kwargs['slug'])
        form = NoteForm(request.POST)
        passw = request.POST['password']
        print(passw)
        if form.is_valid() and passw == CRYPT_PASSWORD:
            notetext = form.cleaned_data['text']
            notetext = crypt(notetext)
            print(notetext)
            note.text = notetext
            # note = form.save()
            note.save()
            return HttpResponseRedirect(reverse('note-update', args=[note.slug]))
        return render(request, 'noteapp/note_form.html', {'form': form})
