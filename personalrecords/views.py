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
from ejercicios.models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  



@login_required(login_url='/login/')
def add_personal_record(request):
    page_title = "Añadir Record Personal"
    user = request.user
    pr = Personal_Record.objects.all()
    clientes = Cliente.objects.all()
    ejercicios = Ejercicio.objects.all()
    if request.method == 'POST':
        form_pr = prForm(request.POST,request.FILES)
        if form_pr.is_valid():
            pr = form_pr.save(commit = False)
            pr.save()            
            return redirect(pr.cliente.get_absolute_url())
    else:
        form_pr = prForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-pr.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def personalrecords(request):
    page_title = "Records Personales"
    user = request.user
    pr = Personal_Record.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(cliente__icontains=query)
        )    
        results = Personal_Record.objects.filter(qset).order_by('-fecha')
        template_name = "resultados-pr.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="prs.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def personal_record(request,recordpersona_id):
    user = request.user
    pr = get_object_or_404(Personal_Record, id=recordpersona_id)
    page_title = pr.cliente     
    template_name ="pr.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_personal_record(request,recordpersona_id):
    page_title = "Editat Record Personal"
    user = request.user
    clientes = Cliente.objects.all()
    ejercicios = Ejercicio.objects.all()
    pr = get_object_or_404(Personal_Record, id=recordpersona_id)
    if request.method == 'POST':
        form_ejercicio = prForm(request.POST,request.FILES,instance=pr)
        if form_ejercicio.is_valid():
            pr = form_ejercicio.save(commit = False)
            pr.save()            
            return redirect(pr.cliente.get_absolute_url())
    else:
        form_ejercicio = prForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-pr.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))