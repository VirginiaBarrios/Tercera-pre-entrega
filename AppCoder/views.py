from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    nombre_curso="Cobol"
    comision_curso=11234

    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)


def cursos(request):
    return render(request, "AppCoder/Cursos.html")

def estudiantes(request):
    return render(request, "AppCoder/Estudiantes.html")

def profesores(request):
    return render(request, "AppCoder/Profesores.html")

def entregables(request):
    return render(request, "AppCoder/Entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la página principal")

def inicio_app(request):
    return render(request, "AppCoder/Inicio.html")

