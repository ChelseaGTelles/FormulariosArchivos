from django import forms
from .models import Libro

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'sinopsis']

class MultiFileForm(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label="Archivos (imágenes o PDF)"
    )
