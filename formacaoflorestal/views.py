# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import FormacaoFlorestal
from .forms import FormacaoFlorestalForm
from django.views.generic import ListView, DetailView
import logging

logger = logging.getLogger(__name__)

def view_list(request) :
    context = {
        'texts' : FormacaoFlorestal.objects.all()
    }
    return render(request, 'formacaoflorestal/list.html', context)

def get_all_formacoes():
    return sorted( FormacaoFlorestal.objects.all(), key=lambda x : x.nome)

class FormacaoFlorestalView(ListView):
    template_name = 'formacaoflorestal/list.html'
    context_object_name = 'formacaoflorestal_list'

    def get_queryset(self):
        return get_all_formacoes()

def create(request):
    form = FormacaoFlorestalForm()
    try:
        if request.method == 'POST':
            logger.info('POST')
            form = FormacaoFlorestalForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/formacaoflorestal/')
            else:
                logger.info( form.errors.as_text())
                return render(request, 'formacaoflorestal/create.html', {'form' : form})
        else:
            return render(request, 'formacaoflorestal/create.html', {'form' : form})
    except:
        logger.info(form)
        logger.info("=>>>> Erro ao criar formacao florestal")
        return render(request, 'formacaoflorestal/create.html', {'form' : form})

def edit(request, id, template_name='formacaoflorestal/edit.html'):
    form = FormacaoFlorestalForm()
    logger.info('>>>edit formacaoflorestal: ' + id)
    try :
        formacaoflorestal = get_object_or_404(FormacaoFlorestal, id=id)
        logger.info(formacaoflorestal)
        form = FormacaoFlorestalForm(request.POST or None, instance=formacaoflorestal)
        logger.info(form.is_valid())
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/formacaoflorestal/')
        else:
            logger.info(form.errors.as_text())
            return render(request, template_name, {'form':form})
    except:
        logger.info(form)
        logger.info("=>>>> Erro ao editar formacaoflorestal")
        return render(request, template_name, {'form' : form})


def delete(request, id, template_name='formacaoflorestal/delete.html'):
    logger.info('delete formacaoflorestal: ' + id)
    try:
        formacaoflorestal = get_object_or_404(FormacaoFlorestal, id=id)
        formacaoflorestal.delete()
        logger.info('deletado!')
        return HttpResponseRedirect('/formacaoflorestal/')
    except:
        logger.info("=>>>> Erro ao deletar especie " + id)
        return render(request, template_name)
