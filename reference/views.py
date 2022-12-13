from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Reference
from .forms import ReferenceForm
from django.views.generic import ListView
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required
def view_list(request) :
    context = {
        'texts' : Reference.objects.all()
    }
    return render(request, 'reference/list.html', context)

class ReferenceView(ListView):
    template_name = 'reference/list.html'
    context_object_name = 'reference_list'

    def get_queryset(self):
        return sorted(Reference.objects.all(), key=lambda x: x.publication)

@login_required
def create(request):
    form = ReferenceForm()
    try:
        if request.method == 'POST':
            form = ReferenceForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/reference/')
            return render(request, 'reference/create.html', {'form' : form})
        return render(request, 'reference/create.html', {'form': form})
    except Exception as e:
        logger.error('[ERROR] creating reference ' + str(e))
        return render(request, 'reference/create.html', {'form': form})

@login_required
def edit(request, id, template_name='reference/edit.html'):
    form = ReferenceForm()
    try :
        forest = get_object_or_404(Reference, id=id)
        form = ReferenceForm(request.POST or None, instance=forest)
        logger.info(form.is_valid())
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/reference/')
        return render(request, template_name, {'form': form})
    except Exception as e:
        logger.error('[ERROR] editing reference' + str(e))
        return render(request, template_name, {'form' : form})

@login_required
def delete(request, id, template_name='reference/delete.html'):
    try:
        forest = get_object_or_404(Reference, id=id)
        forest.delete()
        return HttpResponseRedirect('/reference/')
    except Exception as e:
        logger.error('[ERROR] deleting reference ' + id)
        logger.error(e)
        return render(request, template_name)

