from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from .models import *
from .forms import *
import pandas as pd

# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        usuario = request.user
        perfil = Perfil.objects.get(user = usuario)
        proyectos = Proyecto.objects.filter(autor=usuario)

        return render(request,
                    'inicio.html',
                    {'perfil':perfil,'proyectos':proyectos})
    else:
        return render(request,
                        'inicio.html',
                        {})

def miembros(request):
    miembros = Perfil.objects.all()
    return render(request,
                  'Miembros.html',
                  {'miembros': miembros})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request,
                  'Proyectos.html',
                  {'proyectos': proyectos})

def Vista(request,id):
    proyecto = Proyecto.objects.get(id = id)
    return render(request,
                  'vista.html',
                  {'proyecto':proyecto})


def busqueda(request):
    print(request.GET)
    queryset = request.GET.get('Buscar') 
    if queryset:
        miembros = Perfil.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset)|
            Q(correo__icontains = queryset) 
        ).distinct()
        proyectos = Proyecto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)|
            Q(signalType__nombre__icontains = queryset) 
        ).distinct()
        print(miembros)
        print(proyectos)

    return render(request, 
                  'search.html',
                  {'miembros':miembros,'proyectos':proyectos})

# Vistas con autenticacion 
@login_required
def ProyectosAuth(request):
    usuario = request.user
    proyectos = Proyecto.objects.filter(autor=usuario)
    return render(request,
                  'sesion_activa/mis_proyectos.html',
                  {'proyectos': proyectos})

@login_required
def ProyectosAuthView(request,id,id2):
    usuario = request.user
    proyecto = Proyecto.objects.get(id = id)
    pruebas = Prueba.objects.filter(proyecto = id)
    if id2 == 'w':
        muestras = []
    else:
        id2 = int(id2)
        muestras = Muestra.objects.filter(prueba = id2)
    return render(request,
                  'sesion_activa/proyecto_view.html',
                  {'proyecto':proyecto,'pruebas':pruebas, 'muestras':muestras})

@login_required
def EditProyecto(request):
    return render(request,
                  'sesion_activa/edit_proyecto.html',
                  {})

@login_required
def NewProyecto(request):
    campos = SignalType.objects.all()
    formulario = ProyectoForm(request.POST or None)
    if formulario.is_valid():
        proyecto = formulario.save(commit=False)  # No guardes aún en la base de datos
        proyecto.autor = request.user  # Asigna el autor al usuario activo
        proyecto.save()
        return redirect('inicio')
    else: 
        return render(request,
                  'sesion_activa/edit_proyecto.html',
                  {'campos':campos})


@login_required
def PruebasAuth(request,id):
    usuario = request.user
    proyecto = Proyecto.objects.get(id = id)
    pruebas = Prueba.objects.filter(proyecto = id)
    return render(request,
                  'sesion_activa/Pruebas.html',
                  {'proyecto':proyecto, 'pruebas':pruebas})

@login_required
def MuestrasAuth(request,id,id2):
    usuario = request.user
    proyecto = Proyecto.objects.get(id = id)
    prueba = Prueba.objects.get(id = id2)
    muestras = Muestra.objects.filter(prueba = id2)
    return render(request,
                  'sesion_activa/Muestras.html',
                  {'proyecto':proyecto, 'prueba':prueba, 'muestras':muestras})

@login_required
def VoluntariosAuth(request):
    voluntarios = Voluntario.objects.all().order_by('nombre')
    return render(request,
                  'sesion_activa/voluntarios.html',
                  {'voluntarios' : voluntarios})

@login_required
def AddVoluntario(request):
    formulario = VoluntarioForm(request.POST or None, request.FILES or None )
    if formulario.is_valid():
        formulario.save()
        return redirect('voluntarios')
    else: 
        return render(request,
                  'sesion_activa/añadir_vol.html',
                  {'formulario':formulario})

@login_required
def RecepcionAuth(request):
    return render(request,
                'sesion_activa/recepcion.html',
                {})

@login_required
def borrar(request):
    buffer = Buffer.objects.all()  
    buffer.delete()

    return render(request, 'sesion_activa/recepcion.html')

@login_required
def down(request):
    buffer = Buffer.objects.all()
    s = []
    for obj in buffer:
        a = [obj.ch0, obj.ch1, obj.ch2, obj.ch3, obj.ch4, obj.ch5,
              obj.ch6, obj.ch7, obj.ch8, obj.ch9 , obj.ch10, obj.ch11,
              obj.ch12, obj.ch13, obj.ch14, obj.ch15, obj.ch16, obj.ch17,
              obj.ch18, obj.ch19, obj.ch20, obj.ch21, obj.ch22, obj.ch23]
        s.append(a)

    s = pd.DataFrame(s) 
    s.to_csv('Temp',index=False)

    return render(request, 'sesion_activa/recepcion.html')


def exit(request):
    logout(request)
    return redirect('inicio')
    