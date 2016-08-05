from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from scipy.signal._max_len_seq import max_len_seq
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, blank=True)
    depart = models.CharField(max_length=200, blank = True)
    cell = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return "%s's profile" % self.user


class Project(models.Model):
    prj_id = models.CharField(max_length = 100, unique = True)
    prj_name = models.CharField(max_length = 200, blank = True)

class MedicalBase(models.Model):
    m_id = models.CharField(max_length = 100, unique = True)
    m_depart = models.CharField(max_length=200, blank = True)
    m_bed = models.CharField(max_length = 200, blank = True)
    m_xinfei = models.CharField(max_length = 30, default = "1")
    m_naoxueguan = models.CharField(max_length = 30, default = "1")
    m_chidai = models.CharField(max_length = 30, default = "1")
    m_piantan = models.CharField(max_length = 30, default = "1")
    m_xueya = models.CharField(max_length = 30, default = "1")
    m_guanxinbin = models.CharField(max_length = 30, default = "1")
 
class Patient(models.Model):
    p_id = models.CharField(max_length=100, unique=True)
    p_name = models.CharField(max_length=100, blank = True)
    p_sname = models.CharField(max_length=100, blank = True)
    p_dob = models.DateField(blank=True, default = datetime.today())
    p_age = models.IntegerField(default = 0, blank = True)
    p_height = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    p_weight = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    p_marriage = models.CharField(max_length = 10, blank = True)
    p_edu = models.CharField(max_length = 10, blank = True)
    p_loc = models.CharField(max_length = 400, blank = True)
    p_cell1 = models.CharField(max_length = 50, blank = True)
    p_cell2 = models.CharField(max_length = 50, blank = True)
    p_idcard = models.CharField(max_length = 50, blank = True)

class RelPrjMedPat(models.Model):
    r_prjid = models.ForeignKey(Project)
    r_mid = models.ForeignKey(MedicalBase, related_name = 'rmid', to_field = 'm_id')
    r_pid = models.ForeignKey(Patient, related_name = 'rpid', to_field = 'p_id')
    r_mdepart = models.CharField(max_length = 50, blank = True)
    r_pname = models.CharField(max_length = 50, blank = True)
    

def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)  
      
post_save.connect(create_user_profile, sender=User) 
