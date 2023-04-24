from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio_app, name="incioApp"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
    path('buscandoEstudiante/', buscandoEstudiante, name="buscandoEstudiante"),
    
    path('buscarCurso/', buscarCurso, name="buscarCurso"),
    path('buscandoCurso/', buscandoCurso, name="buscandoCurso"),
    
    path('buscarProfesor/', buscarProfesor, name="buscarProfesor"),
    path('buscandoProfesor/', buscandoProfesor, name="buscandoProfesor"),

    path('buscarEntregable/', buscarEntregable, name="buscarEntregable"),
    path('buscandoEntregable/', buscandoEntregable, name="buscandoEntregable"),
]