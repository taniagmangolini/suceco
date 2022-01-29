# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Registro
from especies.models import Especie
from .forms import RegistroForm, RegistroLoteForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
import csv

logger = logging.getLogger(__name__)

@csrf_exempt
def index(request) :
    '''
    :param request:
    :return: main page
    '''
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
    '''
    :param request:
    :param id:
    :return: list of registers for the selected species
    '''
    especies_list = sorted(Especie.objects.all(), key=lambda x : x.nome)
    especie_selected = None
    template_name = 'registros/list.html'
    id_especie = request.POST.get("id_especie")
    registros = ''
    page_obj = None

    if id_especie is None:
        id_especie = request.session['id_especie']

    if id_especie != None:
        print('ID ESPECIE', id_especie)
        request.session['id_especie'] = id_especie
        registros = Registro.objects.filter(especie=id_especie)
        especie_selected = get_object_or_404(Especie, id=id_especie)

        page = request.GET.get('page', 1)
        paginator = Paginator(registros, 10)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

    contexto = {
        'especies_list' : especies_list,
        'registros_list': registros,
        'id_especie': id_especie,
        'especie_selected' : especie_selected,
        'nr_registros' : len(registros),
        'page_obj' : page_obj
    }
    return render(request, template_name , contexto)

@login_required
def create(request):
    '''
    :param request:
    :return: a new register
    '''
    form = RegistroForm()
    logger.info(request.POST.get('dados_lote', None))
    try:
        if request.method == 'POST':
            logger.info('POST''')
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/registros/')
            else:
                logger.info(form.errors.as_text())
                return render(request, 'registros/create.html', {'form' : form})
        else:
            return render(request, 'registros/create.html', {'form' : form})

    except Exception as e:
        logger.info(form)
        logger.info("[ERROR] creating register")
        return render(request, 'registros/create.html', {'form' : form})


@login_required
def edit(request, id, template_name='registros/edit.html') :
    '''
    :param request:
    :param id:
    :param template_name:
    :return: form with the changed register
    '''
    form = RegistroForm()
    logger.info('editing register' + id)
    try:
        registro = get_object_or_404(Registro, id=id)
        logger.info(registro)
        form = RegistroForm(request.POST or None, instance=registro)
        logger.info(form.is_valid())

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registros/')
        else:
            logger.info(form.errors.as_text())
            return render(request, template_name, {'form': form})

    except Exception as e:
        logger.info(form)
        logger.info("[ERROR] editing register...")
        logger.info(str(e))
        return render(request, template_name, {'form': form})


@login_required
def delete(request, id, template_name='registros/delete.html'):
    '''
    :param request:
    :param id:
    :param template_name:
    :return: registers page
    '''
    try:
        logger.info("Deleting " + id)
        registro = get_object_or_404(Registro, id=id)
        registro.delete()
        return HttpResponseRedirect('/registros/')

    except Exception as e:
        logger.info("[ERROR] deleting register")
        return render(request, template_name)


def export_csv(request):
    '''
    :param request:
    :param id:
    :return: csv file
    '''

    id_especie =  request.session['id_especie']

    especie = Especie.objects.get(pk=id_especie)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + especie.nome + '.csv'
    writer = csv.writer(response)

    if especie:
        registros = Registro.objects.select_related('especie') \
                                    .select_related('formacao_florestal') \
                                    .all(especie=id_especie) \
                                    .values_list('especie__nome',
                                                 'estagio',
                                                 'formacao_florestal__nome',
                                                 'estado',
                                                 'detalhes',
                                                 'referencia')

        for registro in registros :
            writer.writerow(registro)

    return response