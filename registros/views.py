# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Registro
from .forms import RegistroForm
from django.views.generic import ListView, DetailView
import logging

logger = logging.getLogger(__name__)

def view_list(request) :
    context = {
        'texts' : Registro.objects.all()
    }
    return render(request, 'registros/list.html', context)

def get_all_registros():
    return sorted( Registro.objects.all(), key=lambda x : x.especie)

class RegistrosView(ListView):
    template_name = 'registros/list.html'
    context_object_name = 'registros_list'

    def get_queryset(self):
        return get_all_registros()

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