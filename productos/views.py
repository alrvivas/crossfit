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
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  


@login_required(login_url='/login/')
def catalogo(request):
    page_title 	= "Catalogo"
    user        = request.user
    producto 	= Producto.objects.all()     
    categorias 	= Categoria.objects.all() 
    return render_to_response('catalogo.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ver_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    user = request.user
    productos = categoria.producto_set.all()     
    page_title = categoria.nombre
    template_name = "categoria.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def producto(request, producto_slug):
    user        = request.user
    producto = get_object_or_404(Producto, slug=producto_slug)
    page_title = producto.nombre
    template_name="producto.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  


@login_required(login_url='/login/')
def add_categoria(request):
    page_title = "Añadir Categoría"
    user = request.user
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        form_categoria = categoriaForm(request.POST,request.FILES)
        if form_categoria.is_valid():
            categoria = form_categoria.save(commit = False)
            categoria.save()            
            return redirect(categoria.get_absolute_url())
    else:
        form_categoria = categoriaForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-categoria.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_producto(request):
    page_title = "Añadir Categoría"
    user = request.user
    categoria = Categoria.objects.all()
    producto = Producto.objects.all()
    if request.method == 'POST':
        form_producto = productoForm(request.POST,request.FILES)
        if form_producto.is_valid():
            producto = form_producto.save(commit = False)
            producto.save()            
            return redirect(producto.get_absolute_url())
    else:
        form_producto = productoForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-producto.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))