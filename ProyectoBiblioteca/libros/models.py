from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


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


@receiver(post_delete, sender=Documento)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.archivo:
        if os.path.isfile(instance.archivo.path):
            os.remove(instance.archivo.path)
