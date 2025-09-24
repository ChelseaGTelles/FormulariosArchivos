from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, MultiFileForm
from .models import Libro, Documento
from django.contrib import messages

ALLOWED_MIMES = ('application/pdf',)

def index(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def is_allowed_file(f):
    # acepta PDFs y cualquier imagen (image/*)
    if f.content_type in ALLOWED_MIMES or f.content_type.startswith('image/'):
        return True
    return False

def book_list(request):
    books = Libro.objects.all().order_by('-created_at')
    return render(request, 'libros/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        files_form = MultiFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        file_errors = []

        # validar archivos antes de guardar
        for f in files:
            if not is_allowed_file(f):
                file_errors.append(f"{f.name} no es una imagen ni un PDF (content_type: {f.content_type})")

        if book_form.is_valid() and not file_errors:
            book = book_form.save()
            for f in files:
                Documento.objects.create(book=book, file=f)
            messages.success(request, "Libro y archivos guardados correctamente.")
            return redirect('book_list')
        else:
            # mostrar errores combinados
            context = {
                'book_form': book_form,
                'files_form': files_form,
                'file_errors': file_errors
            }
            return render(request, 'libros/book_create.html', context)

    else:
        book_form = BookForm()
        files_form = MultiFileForm()
    return render(request, 'libros/book_create.html', {'book_form': book_form, 'files_form': files_form})

def book_detail(request, pk):
    book = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/book_detail.html', {'book': book})
