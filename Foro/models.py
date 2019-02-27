from django.db import models

#Modelos de la Base de Datos

#Modelo de Estudiante
class Estudiante(models.Model):
    Nombre = models.CharField(max_length=100)   #Nombre del Estudiante
    PrimerApellido = models.CharField(max_length=100)   #Primer Apellido del Estudiante
    SegundoApellido = models.CharField(max_length=100)  #Segundo Apellido del Estudiante
    FechaNacimiento = models.DateTimeField('date published')    #Fecha de Nacimiento del Estudiante

    def __str__(self):
        cadena = self.Nombre + " " + self.PrimerApellido + " " + self.SegundoApellido   #String que se muestra en Admin
        return cadena

# Modelo de Curso
class Curso(models.Model):
    NombreCurso = models.CharField(max_length=100)  #Nombre del Curso
    Modulos = models.PositiveSmallIntegerField(default=0)   #Cantidad de Modulos del Curso

    def __str__(self):
        cadena = self.NombreCurso + " - " + str(self.Modulos)   #String que se muestra en Admin
        return cadena

# Modelo de Nota
class Nota(models.Model):
    NombreCurso = models.ForeignKey(Curso,on_delete=models.CASCADE) #Curso como llave Foranea
    Estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE) #Estudiante como llave Foranea
    Nota = models.PositiveSmallIntegerField(default=0)  #Nota del Estudiante en el Curso

    def __str__(self):
        cadena = str(self.NombreCurso) + " - " +str(self.Estudiante) +" - "+ str(self.Nota) #String que se muestra en Admin
        return cadena