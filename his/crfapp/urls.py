from django.conf.urls import *
from models import *
from views import *

urlpatterns = [
    url(r'^research/$', research_list),
    url(r'^research/(?P<id>[^/]+)/$', view_research, name ='viewPro'),
    url(r'^post$', view_post, name ='viewPro'),
    url(r'^$', login, name='login'),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^regist/$', regist, name = 'regist'),
]