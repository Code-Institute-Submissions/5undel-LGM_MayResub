from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def all_products(request):
    """ A view to return the membership page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'membership/membership.html', context)


@login_required()
def product_detail(request, product_id):
    """ A view to return the membership detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'membership/product_detail.html', context)
