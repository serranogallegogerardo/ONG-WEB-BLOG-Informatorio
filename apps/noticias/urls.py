from django.urls import path
from . import views

from django.conf.urls import include, url

app_name = 'apps.noticia'

urlpatterns = [
    path('agregar/', views.agregar.as_view(), name = 'agregar'),
    path('mostrar/', views.mostrar.as_view(), name = 'mostrar'),
    path('', views.mostrar.as_view()),
    path('modificar/<int:pk>',views.modificar.as_view(), name = 'modificar'),
    path('borrar/<int:pk>', views.BorrarNoticia.as_view(), name= 'borrar'),
    #Orden Descendente
    path('mostrarImg/', views.mostrarImg,name = 'mostrarImg'), 
    #Orden Ascendente
    path('mostrarImgAscendente/', views.mostrarImgAscendente,name = 'mostrarImgAscendente'), 
    path('mostrarImg/<str:categoria>', views.mostrarImgCat, name="mostrarCategoria"),
    path('mostrarCategorias/', views.mostrarCategorias,name = 'mostrarCategorias'),
    path('detalle/<int:pk>', views.mostrarDetalleNoticia.as_view(), name= 'mostrarDetalleNoticia'),
    path('detalles/<int:pk>', views.leerNoticia, name= 'leerNoticia'),
    
    # Agregar categorias 
    path('agregarCategoria/', views.agregarCategoriaView.as_view(), name='agregar_categoria'),
    path('categorias/<str:cates>', views.CategoryList, name='filtrarCategoria'),
    #Borrar categorias
    path('borrarCategoria/<int:pk>', views.borrarCategoria.as_view() , name = 'borrarCategoria'),

    #Borrar comentario
    path('borrarComentario/<int:pk>', views.deleteComentario.as_view(), name='delComentario'),


]
