from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Species
from .forms import SpeciesForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

def get_all_species():
    return sorted(Species.objects.all(), key=lambda x : x.scientific_name)

class SpeciesView(ListView):
    template_name = 'species/list.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return get_all_species()

@login_required
def create(request):
    form = SpeciesForm()
    try:
        if request.method == 'POST':
            form = SpeciesForm(request.POST)
            logger.info(form.is_valid())
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/species/')
            return render(request, 'species/create.html', {'form': form})
        return render(request, 'species/create.html', {'form': form})
    except Exception as e:
        logger.error('[ERROR] creating species ' + str(e))
        return render(request, 'species/create.html', {'form': form})

@login_required
def edit(request, id, template_name='species/edit.html'):
    try :
        species = get_object_or_404(Species, id=id)
        logger.info(species)
        form = SpeciesForm(request.POST or None, instance=species)
        logger.info(form.is_valid())
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/species/')
        logger.info(form.errors.as_text())
        return render(request, template_name, {'form': form})
    except Exception as e:
        logger.error('[ERROR] editing species ' + str(e))
        return render(request, template_name, {'form': form})

@login_required
def delete(request, id, template_name='species/delete.html'):
    try:
        species = get_object_or_404(Species, id=id)
        species.delete()
        return HttpResponseRedirect('/species/')
    except Exception as e:
        logger.error('[ERROR] deleting species' + id + ' ' + str(e))
        return render(request, template_name)

