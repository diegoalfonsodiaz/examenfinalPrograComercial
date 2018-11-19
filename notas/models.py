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
    nombre    = models.CharField(max_length=250)
    seccion   = models.CharField(max_length=250)
    anio      = models.IntegerField()
    materias   = models.ManyToManyField(Materia, through='Asignacion')
    def __str__(self):
        return self.alumno

class Asignacion(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    nota = models.IntegerField()

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class PensumAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)