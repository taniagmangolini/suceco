
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from especies.models import Especie
    
def teste(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'teste.html', {})

