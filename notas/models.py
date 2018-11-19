from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Materia(models.Model):
    nombre  =   models.CharField(max_length=250)
    catedratico = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Pensum(models.Model):
    alumno    = models.CharField(max_length=250)
    nombre_grado    = models.CharField(max_length=250)
    seccion_grado   = models.CharField(max_length=250)
    ciclo      = models.IntegerField() 
    materias   = models.ManyToManyField(Materia, through='Asignacion')
    def __str__(self):
        return self.alumno

class Asignacion(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class PensumAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)




class Carrera(models.Model):
    nombre  =   models.CharField(max_length=250)
    descripccion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Factultad(models.Model):
    nombre    = models.CharField(max_length=250)
    ciclo      = models.IntegerField() 
    carrras   = models.ManyToManyField(Materia, through='AsignacionCarrera')
    def __str__(self):
        return self.nombre

class AsignacionCarrera(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    

class AsignacionCarreraInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class FacultadAdmin(admin.ModelAdmin):
    inlines = (AsignacionCarreraInLine,)


class CarreraAdmin (admin.ModelAdmin):
    inlines = (AsignacionCarreraInLine,)

class Catedratico(models.Model):
    nombre    = models.CharField(max_length=250)
    titulo    = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre