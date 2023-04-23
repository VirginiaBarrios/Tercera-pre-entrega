from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Curso, Entregable
from .forms import ProfesorForm, EstudianteForm, CursoForm, EntregableForm
from django.http import HttpResponse

# Create your views here.

def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = curso()
            curso.nombre = form.cleaned_data['nombre']
            curso.comision = form.cleaned_data['comision']
            curso.save()
            form = CursoForm()
    else:
        form = CursoForm
    cursos = Curso.objects.all() 
    context = {"cursos": cursos, "form": form}
    return render(request, "AppCoder/Cursos.html", context)


def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.apellido = form.cleaned_data['apellido']
            estudiante.email = form.cleaned_data['email']
            estudiante.save()
            form = EstudianteForm()
    else:
        form = EstudianteForm
    estudiantes = Estudiante.objects.all() 
    context = {"estudiantes": estudiantes, "form": form}
    return render(request, "AppCoder/Estudiantes.html", context)


def profesores(request):  #funcion para agregar profesor a el formulario
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm
    profesores = Profesor.objects.all() #llama todos la informacion contenida el objeto profesor y la muestra
    context = {"profesores": profesores, "form": form}
    return render(request, "AppCoder/Profesores.html", context)


def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            entregable = Entregable()
            entregable.nombre = form.cleaned_data['nombre']
            entregable.apellido = form.cleaned_data['apellido']
            entregable.fecha_entrega = form.cleaned_data['fecha_entrega']
            entregable.entregado = form.cleaned_data['entregado']
            entregable.save()
            form = EntregableForm()
    else:
        form = EntregableForm
    entregables = Entregable.objects.all()
    context = {"entregables": entregables, "form": form}
    return render(request, "AppCoder/Entregables.html", context)


def inicio(request):
    return render(request, "")


def inicio_app(request):
    return render(request, "AppCoder/Inicio.html")

def buscarEstudiante(request):
    return render(request, "AppCoder/busquedaEstudiantes.html")

def buscandoEstudiante(request):
    apellidoIngresado = request.GET['apellido']
    if apellidoIngresado!="":
        estudiantes = Estudiante.objects.filter(apellido__icontains=apellidoIngresado)
        print(estudiantes)
        return render(request, "AppCoder/resultadosBusquedaEstudiantes.html", {"estudiantes": estudiantes})
    else:
        return render(request, "AppCoder/busquedaEstudiantes.html", {"mensaje": "Por favor ingrese un apellido"})