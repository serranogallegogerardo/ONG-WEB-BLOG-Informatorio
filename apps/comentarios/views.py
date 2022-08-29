from django.shortcuts import render

from apps.comentarios.models import Comentario
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm

# Create your views here.

def AddComentario(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CommentForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)


class deleteComentario(DeleteView):
	model = Comentario
	template_name = 'comentarios/borrar_comentario.html'
	success_url = reverse_lazy('index')

