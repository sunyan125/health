#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse 

from models import *
from forms import *


def test_edit(request):
    if request.method == 'GET':
        return render(request, 'crfapp/editable.html',{})

@login_required
def medicalbase_edit(request,id):
    if request.method == 'GET':
        return render(request, 'crfapp/medical_base_edit.html',{})


# @login_required   
def update_patient(request,id):
    if request.method == 'POST':
        val = request.POST.get("value")
        cname = request.POST.get("name")
        Patient.objects.filter(id=id).update(**{cname:val})
    return render(request, 'crfapp/profile_edit.html',{})


# @login_required
def patient_edit(request,id):
    if request.method == 'GET':
        patient = Patient.objects.get(id=id)
        return render(request,'crfapp/patient_edit.html',{'patient':patient})

@login_required
def create_crf(request):
    if request.method == 'GET':
        return render(request,'crfapp/create_crf.html',{})

@login_required
def create_crf_detail(request):
    if request.method == 'POST':
        var_id_prj = request.POST['id_prj']
        var_id_m = request.POST['id_m']
        var_id_p = request.POST['id_p']
        var_id_sn = request.POST['id_sn']
        var_id_depart = request.POST['id_depart']
        print "hello"
        prjFlag = Project.objects.filter(prj_id = var_id_prj)
        mFlag = MedicalBase.objects.filter(m_id = var_id_m)
        pFlag = Patient.objects.filter(p_id = var_id_p)
        
#         if prjFlag.exists() == True:
#             return HttpResponse("Failed, project Id exists!")
        if mFlag.exists() == True:
            return HttpResponse("Failed, medical history exists!")
        elif pFlag.exists() == True:    
            return HttpResponse("Failed, medical history exists!")
        else:
            print "need implement" 
            pat = Patient(p_id = var_id_p, p_sname = var_id_sn)
#             prj = Project(prj_id = var_id_prj)
            med = MedicalBase(m_id = var_id_m, m_depart = var_id_depart)
#             prj.save()
            med.save()
            pat.save()
            project = Project.objects.get(prj_id = 1)
            medical = MedicalBase.objects.get(m_id = var_id_m)
            patient = Patient.objects.get(p_id = var_id_p)
            rel = RelPrjMedPat(r_prjid = project, 
                               r_mid = medical, 
                               r_mdepart = var_id_depart, 
                               r_pid = patient,
                               r_pname = var_id_sn)
            rel.save()
            return HttpResponse("Successful")
    else:
        return HttpResponse("Failed")
    
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
        return render(request, 'crfapp/research_list.html', {})

@login_required
def view_research(request):
    return render(request, 'crfapp/research.html', {})
    
@login_required
def view_post(request, id):
    return render(request, 'crfapp/research.html', {})

