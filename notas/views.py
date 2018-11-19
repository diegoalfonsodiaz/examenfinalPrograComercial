from django.shortcuts import render
from django.contrib import messages
from .forms import PensumForm
from notas.models import Pensum, Materia,Asignacion
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def pensum_nuevo(request):
    if request.method == "POST":
        formulario = PensumForm(request.POST)
        if formulario.is_valid():
            pensum = Pensum.objects.create(alumno=formulario.cleaned_data['alumno'],nombre_grado=formulario.cleaned_data['nombre_grado'],seccion_grado=formulario.cleaned_data['seccion_grado'], ciclo = formulario.cleaned_data['ciclo'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, pensum_id = pensum.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pensum Guardado Exitosamente')
    else:
        formulario = PensumForm()
    return render(request, 'notas/pensum_editar.html', {'formulario': formulario})