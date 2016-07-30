#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import *
from forms import *


@login_required
def user_profile(request):
    if request.method == 'GET':
        return render(request, 'crfapp/user_profile.html', {})

@login_required
def research_list(request):
    if request.method == 'GET':
        username = request.user.username
        return render(request, 'crfapp/research_list.html', {'username':username})
    if request.method == 'POST':
        print "need implementation"

@login_required
def view_research(request):
    return render(request, 'crfapp/research.html', {})
    
@login_required
def view_post(request, id):
    return render(request, 'crfapp/research.html', {})

