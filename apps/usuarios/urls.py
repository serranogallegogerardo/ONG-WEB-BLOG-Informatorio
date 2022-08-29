from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrarUsuarios, ModificarUsuario, BorrarUsuario
#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    
    path('agregar/', RegistrarUsuarios.as_view() ,name="agregar"),

    path('modificar/<int:pk>', ModificarUsuario.as_view() ,name="modificar"),
    
    path('borrar/<int:pk>', BorrarUsuario.as_view() ,name="eliminar")
]