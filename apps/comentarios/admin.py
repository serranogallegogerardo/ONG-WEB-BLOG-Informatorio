from django.contrib import admin
from apps.comentarios.models import Comentario
from apps.usuarios.models import Usuario

# Register your models here.

admin.site.register(Comentario)
admin.site.register(Usuario)