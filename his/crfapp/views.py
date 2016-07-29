#coding=utf-8
from django.shortcuts import render, render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
import datetime

from models import *
from forms import *
from django.template.defaultfilters import default
from django.contrib.auth import authenticate

def register(request):
    registered = False;
    if request.method == 'POST':
         print "works"
         user_form = UserForm(data=request.POST)
         profile_form = UserProfileForm(data=request.POST)
         
         if user_form.is_valid() and profile_form.is_valid():
            user = user_form_save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True;
         else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 
                  'registration/registration_form.html', 
                   {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
          
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username, password
        user = authenticate(username = username, password = password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('crfapp/research.html')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'registration/login.html',{})

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

    t=get_template('crfapp/research.html')
    c=RequestContext(request,locals())
    #c=RequestContext(request,{'posts':posts})
    return HttpResponse(t.render(c))

