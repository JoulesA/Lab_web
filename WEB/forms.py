from django import forms 
from .models import *

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class SignalTypeForm(forms.ModelForm):
    class Meta:
        model = SignalType
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = '__all__'

class MuestraForm(forms.ModelForm):
    class Meta:
        model = Muestra
        fields = '__all__'
