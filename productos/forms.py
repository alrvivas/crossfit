#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Categoria,Producto

class categoriaForm(ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'

class productoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

