
from unicodedata import name
from django.shortcuts import render

from apps import noticias
from apps.usuarios.models import Usuario
from .models import Noticia, Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from apps.comentarios.forms import CommentForm
from apps.comentarios.models import Comentario
from django.contrib.auth import views as auth
from django.shortcuts import get_object_or_404
# Create your views here.


# ListaDenoticias = Noticia.objects.first()
# TituloCategoria = Noticia.Categoria
# Categorias = Noticia.objects.first()

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def mostrarCategorias(request):
    categories = Categoria.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'noticias/mostrarCategorias.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

class agregar(CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'noticias/agregar.html'
    success_url = reverse_lazy('index')

class mostrar(ListView):
    model = Noticia
    template_name = 'noticias/mostrar.html'

### ORDENAR FECHA Y MOSTRAR NOTICIAS

def mostrarImg(request): #Orden Descendente

    # Lista de noticias
    #noticia = Noticia.objects.all()
    noticia = Noticia.objects.order_by("-fecha")
       
        # mostrar categorias (listas)
    listaDeCategorias = Categoria.objects.order_by('nombre')

        #----------------------------------
    
    context = {
        'noticia' : noticia,
        'listaDeCategorias': listaDeCategorias,
    } 

    return render(request,'noticias/mostrarImg.html',context)

def mostrarImgAscendente(request): # parecido a un get

    # Lista de noticias
    #noticia = Noticia.objects.all()

    noticia = Noticia.objects.order_by("id")
    # mostrar categorias (listas)
    listaDeCategorias = Categoria.objects.order_by('nombre')

        #----------------------------------
    
    context = {
        'noticia' : noticia,
        'listaDeCategorias': listaDeCategorias,
    } 

    return render(request,'noticias/mostrarImgAscendente.html',context)


def mostrarImgCat(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia = Noticia.objects.filter(categoria = categoria2[0].id)
    context = { 
		'noticia': noticia,
    }

    return render(request,'noticias/mostrarImg.html', context)

class BorrarNoticia(DeleteView):
    model = Noticia
    template_name = 'noticias/borrar.html'
    success_url = reverse_lazy('index')
    
class modificar(UpdateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticias/modificar.html'
    success_url = reverse_lazy('index')


class mostrarDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticias/mostrarDetalleNoticia.html'
  





#||CATEGORIAS --------------------------------#
class agregarCategoriaView(CreateView):
    model = Categoria
    template_name = 'noticias/agregarCategoria.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class borrarCategoria(DeleteView):
    model = Categoria
    template_name = 'noticias/borrarCategoria.html'
    fields = '__all__'
    success_url = reverse_lazy('index')




#-_-_-_-_-_-_-_-_-_| separador |_-_-_-_-_-_-_-_-_-

def CategoryList(request, cates):
    
    cat = Categoria.objects.filter( nombre = cates)
    if len(cat) > 0:
        noticiasFiltradas = Noticia.objects.filter(categoria = cat[0].id)
    c = []
    for dic in Categoria.objects.values('nombre'):
        
        c.append(dic['nombre'])
        

    myContext = {
        'c': c,
        'cates':cates, 
        'noticiasFiltradas':noticiasFiltradas,
    }    

        
    return render(request, 'noticias/filtrarPorCategoria.html', myContext )

#------------------ END CATEGORIAS ---------------------#




#||Vista Detalle ---------------------------------------
""" class mostrarDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticias/mostrarDetalleNoticia.html'
    
    

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
    noticia = Noticia.objects.order_by("-fecha")
    listaDeCategorias = Categoria.objects.order_by('nombre')

    return super().get_context_data(**kwargs)
        #----------------------------------
    
    context = {
        
        'listaDeCategorias': listaDeCategorias,
    } 

    return render(request,'noticias/mostrarDetalleNoticia.html',context) """
#############################################################################    

def leerNoticia(request, pk):
    
    noticia = Noticia.objects.filter(id=pk)
    comentarios = Comentario.objects.filter(noticia=pk)
    post = get_object_or_404(Noticia, pk=pk)
    new_comment = None
    

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid(): 
        # Create Comment object but don't save to database yet
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.noticia_id= pk    

        new_comment.usuario_id= request.user.id
      
        # Save the comment to the database
        new_comment.save()
    else:
        comment_form = CommentForm()


    
    context = {
		'noticia': noticia,
		'comentarios': comentarios,
        'new_comment': new_comment,
        'comment_form': comment_form
	}
    return render(request,'noticias/leerNoticia.html', context)


############## || Borrar comentario (pruebo si poniendolo acá no da error)
class deleteComentario(DeleteView):
	model = Comentario
	template_name = 'comentarios/borrar_comentario.html'
	success_url = reverse_lazy('index')

