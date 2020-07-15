from django.shortcuts import render, get_object_or_404
from .models import Category, Item
from cart2.forms import CartAddProductForm
from cart2.cart import Cart

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    cart = Cart(request)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Item.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'items': items,
        'cart': cart
    }

    return render(request, 'shop/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Item, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/detail.html', context)





