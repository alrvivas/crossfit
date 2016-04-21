#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *


class ordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = ('cliente','estatus_orden','tipo_pago','estatus_cobranza','fecha','subtotal','total','total_peso','saldo',)

class editordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = ('cliente','estatus_orden','tipo_pago','estatus_cobranza','fecha','saldo','observacion',)

class oobservacionForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('observacion',)


class oproductoForm(forms.ModelForm):
    class Meta:
        model = Orden_Producto
        fields = ('orden','producto','precio','cantidad','subtotal_producto','subtotal_peso',) 

class osaldoForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('saldo',)

