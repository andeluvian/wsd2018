from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from django.db.models import Q

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    obj = get_object_or_404(Product, id=product_id)
    context = {"object": obj}


    return render(request, "webshop/product_view.html", context)

def available_products(request):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    queryset = Product.objects.all().filter(~Q(quantity = 0))

    context = {"object_list": queryset}

    return render(request, "webshop/product_list.html", context)
