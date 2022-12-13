from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Register
from species.models import Species
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from suceco._constants import CLASS_TRANSLATOR, CLASS_COLOR
import logging
import csv
import json

logger = logging.getLogger(__name__)

@csrf_exempt
def index(request) :
    '''
    :param request:
    :return: main page
    '''
    species_list = sorted( Species.objects.all(), key=lambda x : x.scientific_name)
    context = {
        'species_list' : species_list,
        'register_list': None,
        'id_species': None,
        'species_selected': None,
        'nr_registers': None
    }
    return render(request, 'register/list.html', context)

@csrf_exempt
def search(request, id=None):
    '''
    Registers for the selected species.
    '''
    species_list = sorted(Species.objects.all(), key=lambda x: x.scientific_name)
    species_selected = None
    template_name = 'register/list.html'
    id_species = request.POST.get("id_species")
    registers = ''
    page_obj = None

    if id_species is None:
        id_species = request.session['id_species']

    if id_species != None:
        request.session['id_species'] = id_species
        registers = Register.objects.filter(species=id_species)
        species_selected = get_object_or_404(Species, id=id_species)

        page = request.GET.get('page', 1)
        paginator = Paginator(registers, 10)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

    pie_chart_data_json = generate_pie_chart(registers)

    context = {
        'species_list' : species_list,
        'register_list': registers,
        'pie_chart' : json.dumps(pie_chart_data_json),
        'id_species': id_species,
        'species_selected' : species_selected,
        'nr_registers' : len(registers),
        'page_obj' : page_obj
    }
    return render(request, template_name, context)


def generate_pie_chart(registers):
    '''
    Generate a pie chart.
    '''
    pie_chart_data = {'Pioneira' :  0,
                      'Secundária Inicial': 0,
                      'Secundária Tardia': 0,
                      'Umbrófila': 0,
                      'Climácica': 0,
                      'Secundária': 0}

    for reg in registers :
        pie_chart_data[CLASS_TRANSLATOR.get(reg.stage)] += 1

    labels = []
    values = []
    colors = []

    for label, count in pie_chart_data.items():
        if count > 0:
            labels.append(label)
            values.append(count)
            colors.append(CLASS_COLOR.get(label))

    pie_chart_data_json = {"labels": labels,
                           "values": values,
                           "colors": colors}

    print(pie_chart_data_json)

    return pie_chart_data_json


@login_required
def create(request):
    '''
    Create a register.
    '''
    form = RegisterForm()
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/register/')
            return render(request, 'register/create.html', {'form': form})
        return render(request, 'register/create.html', {'form': form})

    except Exception as e:
        logger.info('[ERROR] creating a register ' + str(e))
        return render(request, 'register/create.html', {'form': form})


@login_required
def edit(request, id, template_name='register/edit.html') :
    '''
    Updates a register.
    '''
    form = RegisterForm()
    try:
        reg = get_object_or_404(Register, id=id)
        form = RegisterForm(request.POST or None, instance=reg)
        logger.info(form.is_valid())

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/')
        return render(request, template_name, {'form': form})

    except Exception as e:
        logger.error('[ERROR] editing a register' + str(e))
        return render(request, template_name, {'form': form})


@login_required
def delete(request, id, template_name='register/delete.html'):
    '''
    Removes a register.
    '''
    try:
        reg = get_object_or_404(Register, id=id)
        reg.delete()
        return HttpResponseRedirect('/register/')

    except Exception as e:
        logger.error("[ERROR] deleting register " + str(e))
        return render(request, template_name)


def export_csv(request):
    '''
    Generate a csv file for the selected registers.
    '''
    species = Species.objects.get(pk=request.session['id_species'])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + species.scientific_name + '.csv'
    writer = csv.writer(response)

    if species:
        registers = Register.objects.select_related('species') \
                                    .select_related('forest') \
                                    .filter(species=species.id) \
                                    .values_list('species__scientific_name',
                                                 'stage',
                                                 'forest__name',
                                                 'state',
                                                 'reference__publication')

        for reg in registers :
            writer.writerow(reg)

    return response