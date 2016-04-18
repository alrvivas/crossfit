# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from models import *
from cliente.models import *
from productos.models import *
from forms import *
from productos.forms import *
from django.forms.models import modelformset_factory
from django.forms import BaseFormSet, formset_factory
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  



@login_required(login_url='/login/')
def punto_venta(request):
    page_title = "Punto de Venta"
    user = request.user
    productos = Producto.objects.filter(activo = True)
    clientes = Cliente.objects.all()
    orden = Orden.objects.all()
    last_orden = Orden.objects.latest('id')
    tipo_pago = Tipo_Pago.objects.all()
    tipo_abono = Tipo_Abono.objects.all()
    estatus_orden = Estatus_Orden.objects.all()
    estatus_cobranza = Estatus_Cobranza.objects.all()
    OrdenProductoFormSet = modelformset_factory(Orden_Producto,form=oproductoForm,extra=len(productos))
    if request.method == 'POST':
        form_orden = ordenForm(request.POST)
        formset = OrdenProductoFormSet(request.POST,request.FILES)
        if form_orden.is_valid():
            orden = form_orden.save(commit=False)
            orden.save()
            if formset.is_valid():                
                formset.save()            
                return redirect(orden.get_absolute_urle())
    else:
        form_orden = ordenForm()
        formset = OrdenProductoFormSet(queryset=Orden_Producto.objects.none())
    args = {}
    args.update(csrf(request))
    template_name = "punto-venta.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def orden_exitosa(request,orden_id):
    user = request.user
    orden = get_object_or_404(Orden, id=orden_id)
    orden_producto = Orden_Producto.objects.filter(orden=orden)
    page_title = "¡Orden Exitosa!"    
    template_name ="orden-exitosa.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def orden(request,orden_id):
    user = request.user
    orden = get_object_or_404(Orden, id=orden_id)
    orden_producto = Orden_Producto.objects.filter(orden=orden)
    page_title = "Orden"    
    template_name ="orden-exitosa.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def credito_cobranza(request):
    user = request.user
    orden_pendiente = Orden.objects.filter(estatus_cobranza=1)
    orden_abonada = Orden.objects.filter(estatus_cobranza=3)
    page_title = "Credito y Cobranza"    
    template_name ="credito-cobranza.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))