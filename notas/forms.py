from django import forms
from .models import *

class PensumForm(forms.ModelForm):

    class Meta:
        model = Pensum
        fields = ('alumno', 'nombre_grado', 'seccion_grado', 'cliclo', 'materias')




def __init__ (self, *args, **kwargs):
    super(PensumForm, self).__init__(*args, **kwargs)
    self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["materias"].help_text = "Ingrese las materias"
    self.fields["materias"].queryset = Materia.objects.all()