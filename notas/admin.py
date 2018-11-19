from django.contrib import admin
from notas.models import *

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Pensum, PensumAdmin)