# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ipaddress

from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from .forms import InputForm
from .ipcal import *


ip_str = ''
prefix = 0

# Create your views here.
def index(request):
    if request.method == 'POST':        
        input_form = InputForm(data=request.POST)
        if input_form.is_valid():
            clean = input_form.cleaned_data
            print(clean)
            global ip_str,prefix
            ip_str = clean['ip']
            prefix = int(clean['prefix'])
        else:
            print(input_form.errors)
        return redirect("/result")
       
    else:
        print('else')
        input_form = InputForm()
    data = {
        'input_form': input_form
    }
    return render(request, "index.html", data)

def result(request):
    ip = ipaddress.IPv4Address(ip_str)
    context = {
        'ip_full': str(get_ip_network(ip, prefix)),
        'ip': ip_str,
        'prefix' : prefix,
        'network_address' : str(network_address(ip, prefix)),
        'broadcast_address' : str(broadcast_address(ip, prefix)),
        'ip_amount' : host_no(prefix),
        'ip_usable' : usable_host_no(prefix),
        'subnet' : str(gen_subnet(prefix)),
        'class' : get_class(ip),
        'usable_range' : usable_range(ip, prefix)
    }
    # print(ip_str, prefix)
    print(context)
    return render(request, 'result.html', context)
