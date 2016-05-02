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

class entregarodenForm(ModelForm):
    class Meta:
        model = Orden
        fields = ('estatus_orden',)

class orevisionForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('observacion','estatus_orden',)


class oproductoForm(forms.ModelForm):
    class Meta:
        model = Orden_Producto
        fields = ('orden','producto','precio','cantidad','subtotal_producto','subtotal_peso',) 

class osaldoForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('estatus_cobranza','saldo',)

class abonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        fields = '__all__'

class devolucionForm(ModelForm):
    class Meta:
        model = Orden
        fields = ('fecha','orden',)

class caprurardevolucionForm(ModelForm):
    class Meta:
        model = Orden
        fields = ('subtotal','total','total_peso',)