from django.db import models
from apps.noticias.models import Noticia
from apps.usuarios.models import Usuario
# Create your models here.

# si llega a haber algun problema aca, entonces es el from apps...

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField(max_length=200)        #comentario
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return '{}'.format(self.noticia)





        