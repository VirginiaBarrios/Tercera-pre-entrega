from django.shortcuts import render
from .models import Curso, Profesor
from .forms import ProfesorForm
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    nombre_curso="JavaScript"
    comision_curso=54345

    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def agregar_profesor(request):
    nombre_profesor="Miguel"
    apellido_profesor="Rodriguez"
    email_profesor="miguel@rodriguez.com"
    profesion_profesor="Developer"

    profesor=Profesor(nombre=nombre_profesor, apellido=apellido_profesor, email=email_profesor, profesion=profesion_profesor)
    profesor.save()
    respuesta=f"Profesor agregado --- {nombre_profesor} {apellido_profesor} - {profesion_profesor}"
    return HttpResponse(respuesta)


def cursos(request):
    return render(request, "AppCoder/Cursos.html")

def estudiantes(request):
    return render(request, "AppCoder/Estudiantes.html")

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
    return render(request, "AppCoder/Entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la página principal")

def inicio_app(request):
    return render(request, "AppCoder/Inicio.html")

