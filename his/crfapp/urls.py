from django.conf.urls import *
from models import *
from views import *

urlpatterns = [
    url(r'^research/$', research_list),
    url(r'^research/(?P<id>[^/]+)/$', view_research, name ='viewPro'),
    url(r'^post$', view_post, name ='viewPro'),
    url(r'^profile/$',profile_edit),
    url(r'^updateuser/(?P<id>\d+)$', update_user, name ='updateuser'),
    url(r'^create/$', create_crf),
    url(r'^createcrfdetail/$', create_crf_detail, name = 'createcrfdetail'),
    url(r'^patient/(?P<id>\d+)$',patient_edit),
    url(r'^updatepatient/(?P<id>\d+)$', update_patient, name ='updatepatient'),
    url(r'^medical/$',medicalbase_edit),
    url(r'^editable/$', test_edit)
]