# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def result(request):
    context = {}
    return render(request, 'result.html', context)
