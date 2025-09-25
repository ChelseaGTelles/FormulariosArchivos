from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookForm, MultiFileForm
from .models import Libro, Documento

ALLOWED_MIMES = ('application/pdf', 'application/x-pdf', 'application/octet-stream')


def book_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    messages.success(request, "Libro eliminado correctamente.")
    return redirect('book_list')


def book_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    documentos = libro.documents.all()
    return render(request, 'libros/book_detail.html', {
        'libro': libro,
        'documentos': documentos
    })


def is_allowed_file(f):
    return f.content_type in ALLOWED_MIMES or f.content_type.startswith('image/')


def book_list(request):
    libros = Libro.objects.all().order_by('-creado_en')
    return render(request, 'libros/book_list.html', {'libros': libros})


def book_create(request):
    file_errors = []
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        files = request.FILES.getlist('files') 

        for f in files:
            print(f"Archivo recibido: {f.name}, tipo: {f.content_type}")
            if not is_allowed_file(f):
                file_errors.append(f"{f.name} no es PDF ni imagen (MIME: {f.content_type})")

        if book_form.is_valid() and not file_errors:
            libro = book_form.save()
            for f in files:
                Documento.objects.create(libro=libro, archivo=f)

            messages.success(request, "Libro y archivos guardados correctamente.")
            return redirect('book_list')

    else:
        book_form = BookForm()

    return render(request, 'libros/book_create.html', {
        'book_form': book_form,
        'file_errors': file_errors
    })

