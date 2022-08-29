from django.urls import path
from . import views


apps_name = 'apps.comentarios'

urlpatterns = [
    path('addcomentario/', views.AddComentario, name="addcomentario"),
    path('borrarComentario/<int:pk>', views.deleteComentario.as_view(), name='delComentario'),




]


