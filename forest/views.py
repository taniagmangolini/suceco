from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Forest
from .forms import ForestForm
from django.views.generic import ListView
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required
def view_list(request) :
    context = {
        'texts' : Forest.objects.all()
    }
    return render(request, 'forest/list.html', context)

def get_all_forests():
    return sorted( Forest.objects.all(), key=lambda x: x.name)

class ForestView(ListView):
    template_name = 'forest/list.html'
    context_object_name = 'forest_list'

    def get_queryset(self):
        return get_all_forests()

@login_required
def create(request):
    form = ForestForm()
    try:
        if request.method == 'POST':
            logger.info('POST')
            form = ForestForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/forest/')
            logger.info( form.errors.as_text())
            return render(request, 'forest/create.html', {'form' : form})
        return render(request, 'forest/create.html', {'form': form})
    except Exception as e:
        logger.error('[ERROR] creating forest ' + str(e))
        return render(request, 'forest/create.html', {'form': form})

@login_required
def edit(request, id, template_name='forest/edit.html'):
    form = ForestForm()
    try :
        forest = get_object_or_404(Forest, id=id)
        form = ForestForm(request.POST or None, instance=forest)
        logger.info(form.is_valid())
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/forest/')
        return render(request, template_name, {'form': form})
    except Exception as e:
        logger.error('[ERROR] editing forest ' + str(e))
        return render(request, template_name, {'form' : form})

@login_required
def delete(request, id, template_name='forest/delete.html'):
    try:
        forest = get_object_or_404(Forest, id=id)
        forest.delete()
        return HttpResponseRedirect('/forest/')
    except Exception as e:
        logger.error('[ERROR] deleting forest ' + id + ' ' +  str(e))
        return render(request, template_name)

