"""ong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .vista import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('', index,name='index'),
    path('quienesSomos/', about, name='about'),
    path('mision/', causes, name ='causes'),
    path('blog/', blog, name = 'blog'),
    path('contacto/', contact, name = 'contact'),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # URL , Carpeta de origen
    path('noticias/', include('apps.noticias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    


  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

