# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Especie
from .forms import EspecieForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger(__name__)

def get_all_species():
    return sorted( Especie.objects.all(), key=lambda x : x.nome)

class EspeciesView(ListView):
    template_name = 'especie/list.html'
    context_object_name = 'especie_list'

    def get_queryset(self):
        return get_all_species()

@login_required
def create(request):
    form = EspecieForm()
    try:
        if request.method == 'POST':
            logger.info("post")
            form = EspecieForm(request.POST)
            logger.info(form.is_valid())
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/especies/')
            else:
                logger.info( form.errors.as_text())
                return render(request, 'especie/create.html', {'form' : form})
        else:
            return render(request, 'especie/create.html', {'form' : form})
    except:
        logger.info(form)
        logger.info("=>>>> Erro ao criar especie")
        return render(request, 'especie/create.html', {'form' : form})


@login_required
def edit(request, id, template_name='especie/edit.html'):
    logger.info('>>>edit especie: ' + id)
    try :
        especie = get_object_or_404(Especie, id=id)
        logger.info(especie)
        form = EspecieForm(request.POST or None, instance=especie)
        logger.info(form.is_valid())
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/especies/')
        else:
            logger.info(form.errors.as_text())
            return render(request, template_name, {'form':form})
    except:
        logger.info(form)
        logger.info("=>>>> Erro ao editar especie")
        return render(request, template_name, {'form' : form})

@login_required
def delete(request, id, template_name='especie/delete.html'):
    logger.info('delete especie: ' + id)
    try:
        especie = get_object_or_404(Especie, id=id)
        especie.delete()
        logger.info('deletado!')
        return HttpResponseRedirect('/especies/')
    except:
        logger.info("=>>>> Erro ao deletar especie " + id)
        return render(request, template_name)

