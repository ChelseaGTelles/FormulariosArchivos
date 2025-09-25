from django import forms
from .models import Libro

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'sinopsis']

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # habilita múltiples archivos

class MultiFileForm(forms.Form):
    files = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True}),
        label="Selecciona uno o más archivos"
    )
