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
    template_name ="orden.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editar_orden(request,orden_id):
    user = request.user
    orden = get_object_or_404(Orden, id=orden_id)
    estatus_orden = Estatus_Orden.objects.all()
    estatus_cobranza = Estatus_Cobranza.objects.all()
    tipo_pago = Tipo_Pago.objects.all()
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form_orden = editordenForm(request.POST,request.FILES,instance=orden)
        if form_orden.is_valid():
            orden = form_orden.save(commit = False)
            orden.save()            
            return redirect(orden.get_absolute_url())
    else:
        form_orden = editordenForm()
    args = {}
    args.update(csrf(request))
    page_title = "Editar Orden"  
    template_name ="editar-orden.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def credito_cobranza(request):
    user = request.user
    orden_pendiente = Orden.objects.filter(estatus_cobranza=1).order_by('-id')    
    orden_pagadas = Orden.objects.filter(estatus_cobranza=2).order_by('-id')
    orden_abonada = Orden.objects.filter(estatus_cobranza=3).order_by('-id')
    ordenes_revision = Orden.objects.filter(estatus_orden=4).order_by('-id')
    page_title = "Credito y Cobranza"
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(cliente__nombre__icontains=query) 
        )    
        results_op = Orden.objects.filter(qset,estatus_cobranza=1).order_by('-id')        
        results_opa = Orden.objects.filter(qset,estatus_cobranza=2).order_by('-id')
        results_oa = Orden.objects.filter(qset,estatus_cobranza=3).order_by('-id')
        template_name = "resultados-credito-cobranza.html"
        return render_to_response(template_name, {'results_opa':results_opa,'results_op': results_op,'results_oa':results_oa,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results_op = []        
        results_opa = []
        results_oa = []    
    template_name ="credito-cobranza.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def corregir_orden(request,orden_id):
    page_title = "Corregir Orden"
    user = request.user
    productos = Producto.objects.filter(activo = True)
    clientes = Cliente.objects.all()
    orden = get_object_or_404(Orden, id=orden_id)
    tipo_pago = Tipo_Pago.objects.all()
    estatus_orden = Estatus_Orden.objects.all()
    estatus_cobranza = Estatus_Cobranza.objects.all()
    orden_producto = Orden_Producto.objects.filter(orden=orden)
    OrdenProductoFormSet = modelformset_factory(Orden_Producto,form=oproductoForm,extra=len(productos))
    if request.method == 'POST':
        form_orden = ordenForm(request.POST,instance=orden)
        formset = OrdenProductoFormSet(request.POST,request.FILES,queryset=Orden_Producto.objects.filter(orden=orden))
        if form_orden.is_valid() and formset.is_valid():
            orden = form_orden.save(commit=False)
            orden.save()
            formset.save()
            return redirect(orden.get_absolute_urle())
    else:
        form_orden = ordenForm()
        formset = OrdenProductoFormSet(queryset=Orden_Producto.objects.filter(orden=orden))
    args = {}
    args.update(csrf(request))
    template_name = "corregir-orden.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def abonar_orden(request,orden_id):
    user = request.user
    orden = get_object_or_404(Orden, id=orden_id)
    abono = Abono.objects.all()
    abonos = Abono.objects.filter(orden=orden)
    estatus_orden = Estatus_Orden.objects.all()
    estatus_cobranza = Estatus_Cobranza.objects.all()
    tipo_pago = Tipo_Pago.objects.all()
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form_abano = abonoForm(request.POST)
        form_orden = osaldoForm(request.POST,request.FILES,instance=orden)
        if form_orden.is_valid():
            orden = form_orden.save(commit = False)
            orden.save()
            abono = abonoForm.save(commit = False)
            abono.save()            
            return redirect('credito-cobranza')
    else:
        form_abano = abonoForm()
        form_orden = editordenForm()
    args = {}
    args.update(csrf(request))
    page_title = "Abonar Orden"  
    template_name ="abonar-orden.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
