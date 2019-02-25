from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion',{'fields': ['Nombre']}),
    ]

admin.site.register(Estudiante, EstudianteAdmin)
