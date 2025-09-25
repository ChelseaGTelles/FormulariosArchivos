from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm, MultiFileForm
from .models import Libro, Documento
from django.shortcuts import get_object_or_404


ALLOWED_MIMES = ('application/pdf',)

def book_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    documentos = libro.documents.all()  
    return render(request, 'libros/book_detail.html', {'libro': libro, 'documentos': documentos})


def is_allowed_file(f):
    return f.content_type in ALLOWED_MIMES or f.content_type.startswith('image/')


def book_list(request):
    libros = Libro.objects.all().order_by('-creado_en')
    return render(request, 'libros/book_list.html', {'libros': libros})


def book_create(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        files_form = MultiFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files') 
        file_errors = []

        for f in files:
            if not is_allowed_file(f):
                file_errors.append(f"{f.name} no es PDF ni imagen")

        if book_form.is_valid() and not file_errors:
            libro = book_form.save()
            for f in files:
                Documento.objects.create(libro=libro, archivo=f)

            messages.success(request, "Libro y archivos guardados correctamente.")
            return redirect('book_list')

        return render(request, 'libros/book_create.html', {
            'book_form': book_form,
            'files_form': files_form,
            'file_errors': file_errors
        })

    book_form = BookForm()
    files_form = MultiFileForm()
    return render(request, 'libros/book_create.html', {
        'book_form': book_form,
        'files_form': files_form
    })
