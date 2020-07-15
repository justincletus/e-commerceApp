from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem

class DetailCart(DetailView):
    model = Cart
    template_name = 'cart/detail_cart.html'

class ListCart(ListView):
    model = Cart
    template_name = 'cart/cart_list.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cart/create_cart.html'

class UpdateCart(UpdateView):
    model = Cart
    template_name = 'cart/update_cart.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cart/delete_cart.html'

# CartItem

class DetailCartItem(DetailView):
    model = CartItem
    template_name = 'cart_item/cart_item.html'

class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name = 'cart_item/cart_item_list.html'

class CreateCartItem(CreateView):
    model = CartItem
    template_name = 'cart_item/cart_item_create.html'

class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cart_item/cart_item_update.html'

class DeleteCartItem(DeleteView):
    model = CartItem
    template_name = 'cart_item/cart_item_delete.html'
