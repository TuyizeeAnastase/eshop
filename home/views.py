from django.shortcuts import render
from products.models import Category,Products
from django.shortcuts import render, get_object_or_404

def home(request):

    categories=Category.objects.all()
    products=Products.objects.all()

    category_men = Category.objects.get(name='men')
    category_women = Category.objects.get(name='women')
    category_child = Category.objects.get(name='child')

    products_men = Products.objects.filter(category=category_men)
    products_women=Products.objects.filter(category=category_women)
    products_child=Products.objects.filter(category=category_child)


    context={
        'categories':categories,
        'products':products,
        'products_men':products_men,
        'products_women':products_women,
        'products_child':products_child
    }

    return render(request, 'home.html',context)

def product(request,product_id):
    product = get_object_or_404(Products, pk=product_id)

    context={
        'product':product
    }

    return render(request,'product.html',context)

def search(request):
    products=Products.objects.all()

    context={
        'products':products
    }

    return render(request,'search.html',context)


def category_products(request,id,slug):
    catdata=Category.objects.get(pk=id)
    products=Products.objects.filter(category_id=id)
    context={
        'products':products,
        'catdata':catdata
    }
    return render(request,'category_products.html',context)