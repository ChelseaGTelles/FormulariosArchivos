from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, blank=True)
    sinopsis = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Documento(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='documents')
    archivo = models.FileField(upload_to='documents/%Y/%m/%d/')
    subido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.archivo.name
