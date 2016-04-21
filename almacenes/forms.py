#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import Almacen

class almacenForm(ModelForm):
	class Meta:
		model = Almacen
		fields = '__all__'
