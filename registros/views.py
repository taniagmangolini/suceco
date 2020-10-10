# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Registro
from especies.models import Especie
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def index(request) :
    especies_list =   sorted(  Especie.objects.all(), key=lambda x : x.nome)
    contexto = {
        'especies_list' : especies_list,
        'registros_list': None,
        'id_especie': None,
        'especie_selected': None,
        'nr_registros': None
    }
    return render(request, 'registros/list.html', contexto)

@csrf_exempt
def search(request, id=None):
    especies_list = sorted(Especie.objects.all(), key=lambda x : x.nome)
    especie_selected = None
    template_name = 'registros/list.html'
    id_especie = request.POST.get("id_especie")
    registros = ''

    if id_especie != None:
        registros = Registro.objects.filter(especie=id_especie)
        especie_selected = get_object_or_404(Especie, id=id_especie)

    contexto = {
        'especies_list' : especies_list,
        'registros_list': registros,
        'id_especie': None,
        'especie_selected' : especie_selected,
        'nr_registros' : len(registros)
    }

    return render(request, template_name , contexto )

@login_required
def create(request):
    form = RegistroForm()
    try:
        if request.method == 'POST':
            logger.info('POST')
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/registros/')
            else:
                logger.info( form.errors.as_text())
                return render(request, 'registros/create.html', {'form' : form})
        else:
            return render(request, 'registros/create.html', {'form' : form})
    except:
        logger.info(form)
        logger.info("=>>>> Erro ao criar registros")
        return render(request, 'registros/create.html', {'form' : form})

@login_required
def edit(request, id, template_name='registros/edit.html') :
        form = RegistroForm()
        logger.info('>>>edit registros: ' + id)
        try :
            registro = get_object_or_404(Registro, id=id)
            logger.info(registro)
            form = RegistroForm(request.POST or None, instance=registro)
            logger.info(form.is_valid())
            if form.is_valid() :
                form.save()
                return HttpResponseRedirect('/registros/')
            else :
                logger.info(form.errors.as_text())
                return render(request, template_name, {'form' : form})
        except :
            logger.info(form)
            logger.info("=>>>> Erro ao editar registros")
            return render(request, template_name, {'form' : form})

@login_required
def delete(request, id, template_name='registros/delete.html') :
        logger.info('delete registros: ' + id)
        try :
            registro = get_object_or_404(Registro, id=id)
            registro.delete()
            logger.info('deletado!')
            return HttpResponseRedirect('/registros/')
        except :
            logger.info("=>>>> Erro ao deletar registro " + id)
            return render(request, template_name)