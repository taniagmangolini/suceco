# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Registro
from especies.models import Especie
from formacaoflorestal.models import FormacaoFlorestal
from .forms import RegistroForm, RegistroLoteForm
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
    logger.info("Lote:")
    logger.info(request.POST.get('dados_lote', None))
    try:
        if request.method == 'POST':
            logger.info('POST''')
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
def create_lote(request):
    form = RegistroLoteForm()
    registro = Registro()
    dados_lote =  request.POST.get('dados_lote', '')
    vegetacao_nome =  request.POST.get('formacao_florestal', '')
    estado = request.POST.get('estado', '')
    referencia = request.POST.get('referencia', '')
    detalhes = request.POST.get('detalhes', '')
    especies_estagios = []

    try :
        if dados_lote == '' :
            return render(request, 'registros/create_lote.html', {'form' : form})
        else:

            try :
                vegetacao = FormacaoFlorestal.objects.get(nome=vegetacao_nome)
                logger.info('formacao: ' + vegetacao.nome)
            except FormacaoFlorestal.DoesNotExist :
                vegetacao = None

            especies_estagios = str.split(dados_lote, ',')
            logger.info(especies_estagios)

            for i in especies_estagios:
                logger.info(i)
                especie = None
                especie_estagio = str.split(i, ':')
                estagio = ''
                especie_nome = ''

                try:
                    logger.info(especie_estagio[0])
                    logger.info(especie_estagio[1])
                    especie_nome = especie_estagio[0].strip()
                    estagio = especie_estagio[1].strip()
                except:
                    logger.info('split error')

                if  estagio != '' and especie_nome != '':
                    try:
                        especie  =  Especie.objects.get(nome=especie_nome)
                        logger.info('especie: ' + especie.nome)
                    except:
                        if (especie == None):
                            new_especie = Especie()
                            new_especie.nome =  especie_nome
                            new_especie.save()
                            logger.info('especie add: ' +  especie_nome)
                            especie = Especie.objects.get(nome=especie_nome)

                logger.info('especie: ' + especie.nome)
                logger.info('vegetacao: ' + vegetacao.nome)

                if(especie != None and vegetacao != None):
                    logger.info('creating registro')
                    registro = Registro()
                    registro.especie = especie
                    registro.estagio = estagio
                    registro.formacao_florestal = vegetacao
                    registro.estado = estado
                    registro.referencia = referencia
                    registro.detalhes = detalhes
                    logger.info('saving')
                    registro.save()
                    logger.info('saved')

        return HttpResponseRedirect('/registros/')
    except:
        logger.info("=>>>> Erro ao criar registros")
        return render(request, 'registros/create_lote.html', {'form' : form})



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