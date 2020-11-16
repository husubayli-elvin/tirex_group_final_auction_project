from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('-id')
        context['release_calendar_products'] = Product.objects.order_by('-id')[:4]
        return context


class SingleView(DetailView):
    model = Product
    template_name = 'single.html'
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['same_brand'] = Product.objects.filter(brand__title = product.brand.title)
        context['sizes'] = Product_property.objects.order_by('-id')
        return context


class SellView(TemplateView):
    template_name = 'sell.html'


class SellSingleView(DeleteView):
    template_name = 'sell_single.html'


class SellConfirmationView(DetailView):
    template_name = 'sell_confirmation.html'