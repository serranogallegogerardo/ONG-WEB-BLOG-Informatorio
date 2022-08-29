from django.db import models
from ckeditor.fields import RichTextField
from apps.usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

# Create your models here.
class Noticia(models.Model):

    titulo = models.CharField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = RichTextField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='noticia', default='noticia/default.png')
  
    def __str__(self):
        return self.titulo

