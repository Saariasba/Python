from django.contrib import admin
from .models import Estudiante,Curso

class EstudianteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['Nombre']}),
        ('', {'fields': ['PrimerApellido']}),
        ('', {'fields': ['SegundoApellido']}),
        ('Date information', {'fields': ['FechaNacimiento'], 'classes': ['collapse']}),
    ]

class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['NombreCurso'],}),
        ('', {'fields': ['Modulos']}),
    ]

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)