from django.conf.urls import *
from models import *
from views import *

urlpatterns = [    
    url(r'^product/create/$', create_product, name = 'createPro'),
    url(r'^product/list/$', list_product, name = 'listPro'),
    url(r'^product/edit/(?P<id>[^/]+)/$', edit_product, name ='editPro'),
    url(r'^product/view/(?P<id>[^/]+)/$', view_product, name ='viewPro'),
    url(r'^store/$', store_view, name='storeView'),
    url(r'^cart/view/$', view_cart, name ='cartView'),
    url(r'^cart/add/(?P<id>[^/]+)/$', add_to_cart, name = 'addItem'),
    url(r'^cart/clean/', clean_cart, name = 'cleanItem'),
]