from django.contrib import admin
from .models import Libro, Documento

class DocumentInline(admin.TabularInline):
    model = Documento
    extra = 0

@admin.register(Libro)
class BookAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]

@admin.register(Documento)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('archivo', 'libro', 'subido_el')