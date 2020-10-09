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
    return sorted( Registro.objects.all(), key=lambda x : x.nome)

class RegistrosView(ListView):
    template_name = 'registros/list.html'
    context_object_name = 'registros_list'

    def get_queryset(self):
        return get_all_registros()
