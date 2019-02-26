from django.db import models

#Modelos de la Base de Datos

#Modelo de Estudiante
class Estudiante(models.Model):
    Nombre = models.CharField(max_length=100)
    PrimerApellido = models.CharField(max_length=100)
    SegundoApellido = models.CharField(max_length=100)
    FechaNacimiento = models.DateTimeField('date published')

    def __str__(self):
        cadena = self.Nombre + " " + self.PrimerApellido + " " + self.SegundoApellido
        return cadena

# Modelo de Curso
class Curso(models.Model):
    NombreCurso = models.CharField(max_length=100)
    Modulos = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        cadena = self.NombreCurso + " - " + str(self.Modulos)
        return cadena

# Modelo de Nota
class Nota(models.Model):
    NombreCurso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Nota = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        cadena = str(self.NombreCurso) + " - " +str(self.Estudiante) +" - "+ str(self.Nota)
        return cadena