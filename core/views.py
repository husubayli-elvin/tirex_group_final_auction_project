from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sneakers'] =  [i for i in Product.objects.order_by('-id') if i.category.title == "Sneakers"][:5]
        context['release_calendar_products'] = [i for i in Product.objects.order_by('-id') if i.category.title == "Sneakers"][:4]
        return context

class StreetwearView(TemplateView):
    template_name = 'streetwear.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streetwear'] =  [i for i in Product.objects.order_by('-id') if i.category.title == "Wear"][:5]
        context['release_calendar_products'] = [i for i in Product.objects.order_by('-id') if i.category.title == "Wear"][:4]
        return context

class BrowseListView(ListView):
    model = Product
    context_object_name = 'browse_list'
    template_name = 'browse.html'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AboutUsView(TemplateView):
    template_name = "about.html"

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

class SellProductView(DetailView):
    model = Product
    template_name = 'sell_confirmation.html'