from django import forms
from django.forms import ModelForm 
from django.forms import widgets #permite definir la configuración de los datos de entrada del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Gato

class GatoForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Gato 
        fields = ['chip', 'nombre', 'raza', 'categoria']
        labels = {
            'chip': 'Chip',
            'nombre': 'Nombre',
            'raza': 'Raza',
            'categoria': 'Categoria',
        }
        widgets={
            'chip': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite el n° de chip',
                    'id': 'chip'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Escriba el nombre',
                    'id': 'nombre'
                }
            ),
            'raza': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'DPC O DPL',
                    'id': 'raza'
                }
            ),
            'categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
        }

