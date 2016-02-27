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
def add_ejercicio(request):
    page_title = "Añadir Ejercicio"
    user = request.user
    ejercicio = Ejercicio.objects.all()
    if request.method == 'POST':
        form_ejercicio = ejercicioForm(request.POST,request.FILES)
        if form_ejercicio.is_valid():
            ejercicio = form_ejercicio.save(commit = False)
            ejercicio.save()            
            return redirect(ejercicio.get_absolute_url())
    else:
        form_ejercicio = ejercicioForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-ejercicio.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ejercicios(request):
    page_title = "Ejercicios"
    user = request.user
    ejercicios = Ejercicio.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )    
        results = Ejercicio.objects.filter(qset).order_by('-id')
        template_name = "resultados-ejercicio.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="ejercicios.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def ejercicio(request,ejercicio_id):
    user = request.user
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    page_title = ejercicio.nombre     
    template_name ="ejercicio.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_ejercicio(request,ejercicio_id):
    page_title = "Editat Ejercicio"
    user = request.user
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    if request.method == 'POST':
        form_ejercicio = ejercicioForm(request.POST,request.FILES,instance=ejercicio)
        if form_ejercicio.is_valid():
            ejercicio = form_ejercicio.save(commit = False)
            ejercicio.save()            
            return redirect(ejercicio.get_absolute_url())
    else:
        form_ejercicio = ejercicioForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-ejercicio.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))