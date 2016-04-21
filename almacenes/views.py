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
from productos.models import *
from ventas.models import *
from forms import *
import datetime
from django.db.models import Q  


@login_required(login_url='/login/')
def add_almacen(request):
    page_title = "Añadir Almacén"
    user = request.user
    almacen = Almacen.objects.all()
    if request.method == 'POST':
        form_almacen = almacenForm(request.POST,request.FILES)
        if form_almacen.is_valid():
            almacen = form_almacen.save(commit = False)
            almacen.save()            
            return redirect(almacen.get_absolute_url())
    else:
        form_almacen = almacenForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-almacen.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def almacenes(request):
    page_title = "Almacenes"
    user = request.user
    almacenes = Almacen.objects.all()    
    query = request.GET.get('q', '')            
    template_name ="almacenes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def almacen(request,almacen_id):
    user = request.user
    almacen = get_object_or_404(Almacen, id=almacen_id)
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(categoria=categorias).order_by('orden')
    ordenes_pendientes = Orden.objects.filter(estatus_orden=1).order_by('-id')
    ordenes_entregadas = Orden.objects.filter(estatus_orden=2).order_by('-id')[:20]
    ordenes_canceladas = Orden.objects.filter(estatus_orden=3).order_by('-id')
    ordenes_revision = Orden.objects.filter(estatus_orden=4).order_by('-id')
    page_title = almacen.nombre     
    template_name ="almacen.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_almacen(request,almacen_id):
    page_title = "Editat Almacén"
    user = request.user
    almacen = get_object_or_404(Almacen, id=almacen_id)
    if request.method == 'POST':
        form_almacen = almacenForm(request.POST,request.FILES,instance=almacen)
        if form_cliente.is_valid():
            almacen = form_almacen.save(commit = False)
            almacen.save()            
            return redirect(almacen.get_absolute_url())
    else:
        form_almacen = almacenForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-almacen.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))