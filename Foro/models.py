from django.db import models

#Modelos de la Base de Datos

#Modelo de Estudiante
class Estudiante(models.Model):
    Nombre = models.CharField(max_length=100)
    PrimerApellido = models.CharField(max_length=100)
    SegundoApellido = models.CharField(max_length=100)
    FechaNacimiento = models.DateTimeField('date published')

    def __str__(self):
        cadena = {(0) , (1)}
        return self.cadena

#Modelo de Curso
class Curso(models.Model):
    NombreCurso = models.CharField(max_length=100)
    


    def __str__(self):
        return self.NombreCurso
