from django import forms
from .models import Note


class TitleNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', )


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text', )
