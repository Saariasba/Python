from django.contrib import admin
from .models import Estudiante,Curso,Nota

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

class NotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['NombreCurso'],}),
        ('', {'fields': ['Estudiante']}),
        ('', {'fields': ['Nota']}),
    ]

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Nota, NotaAdmin)