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
from django.template.defaultfilters import default

class UserLoginForm(forms.Form): 
    uname = forms.CharField(label='用户名',max_length=100)
    passwd = forms.CharField(label='密码',widget=forms.PasswordInput())


def login(req):
    if req.method == 'POST':
        ulf = UserLoginForm(req.POST)
        if ulf.is_valid():
            uname = ulf.cleaned_data['uname']
            passwd = ulf.cleaned_data['passwd']
            
            user = User.objects.filter(username__exact = uname,password__exact = passwd)
            if user:
                response = HttpResponseRedirect('crfapp/research.html')
                response.set_cookie('uname',uname,3600)
                return response
            else:
                return HttpResponseRedirect('crfapp/login.html')
    else:
        ulf = UserLoginForm()
    return render_to_response('crfapp/login.html',{'ulf':ulf},context_instance=RequestContext(req))
        

class UserViewForm(forms.Form): 
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    role = forms.CharField(label='角色', max_length=30)
    gender = forms.CharField(label='性别', max_length = 30)
    depart = forms.CharField(label='部门', max_length=200)
    cell = forms.CharField(label='电话', max_length=100)


def regist(req):
    if req.method == 'POST':
        uvf = UserViewForm(req.POST)
        if uvf.is_valid():
            username = uvf.cleaned_data['username']
            password = uvf.cleaned_data['password']
            role = uvf.cleaned_data['role']
            gender = uvf.cleaned_data['gender']
            depart = uvf.cleaned_data['depart']
            cell = uvf.cleaned_data['cell']
            User.objects.create(username= username,password=password, role = role, 
                                gender = gender, depart = depart, cell = cell)
            return HttpResponse('regist success!!')
    else:
        uvf = UserViewForm()
    return render_to_response('crfapp/regist.html',{'uvf':uvf}, context_instance=RequestContext(req))

def logout(req):
    response = HttpResponse('logout !!')
    response.delete_cookie('uname')
    return response

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

