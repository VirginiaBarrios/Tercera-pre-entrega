from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio_app, name="incioApp"),
    path('crear_curso/', crear_curso),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
]