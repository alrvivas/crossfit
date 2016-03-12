#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *


class ordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class oobservacionForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('observacion',)


class oproductoForm(forms.ModelForm):
    class Meta:
        model = Orden_Producto
        fields = '__all__'

class osaldoForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('saldo',)

