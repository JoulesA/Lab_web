from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('miembros', views.miembros, name='miembros'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('proyecto_<int:id>', views.Vista, name='Vista'),
    path('busqueda', views.busqueda, name='busqueda'),

    path('mis_proyectos', views.ProyectosAuth, name = 'ProyectosAuth'),
    path('mis_proyectos/edit', views.EditProyecto, name = 'EditProyecto'),
    path('mis_proyectos/new', views.NewProyecto, name = 'NewProyecto'),
    path('ver_proyecto_<int:id>_<str:id2>', views.ProyectosAuthView, name = 'VerProyecto'),

    path('proyecto_<int:id>/pruebas', views.PruebasAuth, name = 'Pruebas'),
    path('proyecto_<int:id>/prueba_<int:id2>/muestras', views.MuestrasAuth, name = 'Muestras'),


    path('voluntarios', views.VoluntariosAuth, name = 'voluntarios'),
    path('voluntarios/new', views.AddVoluntario, name = 'add_voluntario'),
    path('recepcion/', views.RecepcionAuth, name = 'recepcion'),
    path('recepcion/borrado', views.RecepcionAuth, name = 'recepcion_borrado'),
    path('recepcion/descarga', views.RecepcionAuth, name = 'recepcion_descarga'),
    
    path('exit/', views.exit, name='exit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)