from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('depotapp/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_product(request):
  
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_product(request, id):
    product_instance = Product.objects.get(id=id)

    t=get_template('depotapp/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('depotapp/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def store_view(request):
    products = Product.objects.all()
    t = get_template('depotapp/store_view.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def  view_cart(request):
    cart = request.session.get("cart",None)
    t = get_template('depotapp/view_cart.html')
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def add_to_cart(request,id):
    product = Product.objects.get(id = id)
    cart = request.session.get("cart",None)
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
    cart.add_product(product)
    request.session['cart'] = cart
    return view_cart(request)


def clean_cart(request):
    request.session['cart'] = Cart()
    return view_cart(request)