# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Especie
from .forms import EspecieForm
from django.views.generic import ListView, DetailView
import logging

logger = logging.getLogger(__name__)

def teste(request):
     texts = ['Lorem ipsum dolor sit amet, consectetur adipisicing ']
     context = {
    	'title':'django e-commerce',
    	'texts':texts
     }
     return render(request, 'especie/list.html', context)


def view_list(request) :
    context = {
        'texts' : Especie.objects.all()
    }
    return render(request, 'especie/list.html', context)

def get_all_species():
    return sorted( Especie.objects.all(), key=lambda x : x.nome)

class IndexView(ListView):
    template_name = 'especie/list.html'
    context_object_name = 'especie_list'

    def get_queryset(self):
        return get_all_species()

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

#class EspecieDetailView(DetailView):
#    model = Especie
#    template_name = 'especie/detail.html'

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

