from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# Create your views here.

# app specific files

#from models import *
#from forms import *

def research_list(request):
    t=get_template('crfapp/research_list.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def view_research(request, id):
    # product_instance = Product.objects.get(id=id)

    t=get_template('crfapp/research.html')
    c=RequestContext(request,locals())
    #c=RequestContext(request,{'posts':posts})
    return HttpResponse(t.render(c))

def view_post(request, id):
    # product_instance = Product.objects.get(id=id)

    # t=get_template('crfapp/research.html')
    c=RequestContext(request,locals())
    #c=RequestContext(request,{'posts':posts})
    return HttpResponse(t.render(c))