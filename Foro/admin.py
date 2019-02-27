from django.contrib import admin
from .models import Estudiante,Curso,Nota

#Clases que se organizan en el Admin

#Admin de Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['Nombre']}),
        ('', {'fields': ['PrimerApellido']}),
        ('', {'fields': ['SegundoApellido']}),
        ('Date information', {'fields': ['FechaNacimiento'], 'classes': ['collapse']}),
    ]

#Admin de Curso
class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['NombreCurso'],}),
        ('', {'fields': ['Modulos']}),
    ]

#Admin de Nota
class NotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['NombreCurso'],}),
        ('', {'fields': ['Estudiante']}),
        ('', {'fields': ['Nota']}),
    ]

admin.site.register(Estudiante, EstudianteAdmin)    #Se registra el Modelo en el admin
admin.site.register(Curso, CursoAdmin)  #Se registra el Modelo en el admin
admin.site.register(Nota, NotaAdmin)    #Se registra el Modelo en el admin