from django import forms
from models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'depart', 'cell')
        
class RelPrjMedPatForm(forms.ModelForm):
    class Meta:
        model = RelPrjMedPat
        fields = ('r_prjid', 'r_mid', 'r_mdepart', 'r_pid', 'r_pname')
      
# class MedicalBase(forms.ModelForm):
#     class Meta:
#         model = MedicalBase
#         fields = ('m_id', 'm_depart', 'm_bed',  'm_xinfei', 'm_naoxueguan', 'm_chidai', 'm_piantan', 'm_xueya', 'm_guanxinbin')
        
