#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from models import *
from forms import *


def test_edit(request):
    if request.method == 'GET':
        return render(request, 'crfapp/editable.html',{})

@login_required   
def update_user(request,id):
    if request.method == 'POST':
        val = request.POST.get("value")
        cname = request.POST.get("name")
        if cname == "username" or cname == "email":
            User.objects.filter(id=id).update(**{cname:val})
        else:
            UserProfile.objects.filter(id=id).update(**{cname:val})
        return render(request, 'crfapp/profile_edit.html',{})
    

@login_required
def profile_edit(request):
    if request.method == 'GET':
        return render(request,'crfapp/profile_edit.html',{})
#     if request.method =='POST':
#         print "POST Request"
#         user_form = UserForm(instance=request.user,data=request.POST)
# 
#         profile_form = UserProfileForm(instance=request.user.profile,data=request.POST)
# 
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request,'Profile updated successfully')
# 
#         else:
#             messages.error(request,'Error updating your profile')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = UserProfileForm(instance=request.user.userprofile)
#         print user_form.instance.username
# 
#     context = {
#         'user_form':user_form,
#         'profile_form': profile_form
#     }
    
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

