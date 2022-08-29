from django.shortcuts import render
from .models import Usuario
from .forms import registroUsuarios
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class RegistrarUsuarios(CreateView):
	model = Usuario
	form_class = registroUsuarios
	template_name = 'usuario/register.html'
	success_url = reverse_lazy('apps.usuario:login')

class ModificarUsuario(UpdateView):
	model = Usuario
	form_class = registroUsuarios
	template_name = 'usuario/modificar.html'


class BorrarUsuario(DeleteView):
	model = Usuario
	template_name = 'usuario/usuario_confirm_delete.html'
	success_url = reverse_lazy('index')