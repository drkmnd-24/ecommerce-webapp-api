from django.shortcuts import render, get_object_or_404

from .models import *


def all_products(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)

    context = {'products': products}
    return render(request, 'store/home.html', context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True))
    return render(request, "products/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    context = {'product': product}
    return render(request, 'products/detail.html', context)

