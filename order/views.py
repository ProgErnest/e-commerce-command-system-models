from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    # template_name = ".html"

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    fields = ["name","price", "stock"]
    success_url = reverse_lazy("products_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields= ["name","price","stock"]    
    success_url = reverse_lazy("products_list")
