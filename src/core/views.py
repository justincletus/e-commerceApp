from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Product, Category, UserProfile

class ProductDetailView(DetailView):
    model = Product
    template_name = "core/product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "core/products.html"

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "core/product_create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "core/product_update.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "core/product_delete.html"
