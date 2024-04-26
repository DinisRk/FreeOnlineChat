from django.urls import  path
from . import views
from bootstrap5 import bootstrap

app_name = 'myapp'
urlpatterns = [
path('', views.index, name='index'),
path('inicio.html', views.inicio, name='inicio'),
path('registro.html', views.registro, name='registro'),
path('entrada.html', views.entrada, name='entrada'),
path('eliminar_comentario.html/<int:comments_id>/', views.eliminar_comentario, name='eliminar_comentario'), # Corregido el patrón de URL
path('editar_comentario.html/<int:comments_id>/', views.editar_comentario, name='editar_comentario'), # Corregido el patrón de URL
path('home.html', views.home, name='home'),



]
