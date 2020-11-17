from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property, Question
from .forms import AskQuestionForm, ProductTransactionForm
from django.views.generic.edit import FormMixin

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        title = self.request.GET.get('title')
        queryset = Product.objects.order_by('-id')

        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

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
        context['sizes'] = Property.objects.order_by('-id')
        return context

class SellProductView(FormMixin, DetailView):
    model = Product
    template_name = 'sell_confirmation.html'
    form_class = ProductTransactionForm
    context_object_name = 'selling_product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['highest_bid'] = [i for i in User_bids.objects.filter(product=product).order_by('price') if i.is_sell == False][:1]
        context['lowest_ask'] = [i for i in User_bids.objects.filter(product=product).order_by('-price') if i.is_sell == True][:1]
        return context

    def get_success_url(self):
        return reverse_lazy('core:product-detail', kwargs={'slug':self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_sell = True
        form.instance.product = self.get_object()
        print(form.instance.is_sell)
        form.save()
        return super().form_valid(form)
    

class SellSizeProductView(DetailView):
    model = Product
    template_name = 'sell_single.html'
    context_object_name = 'selling_size_product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['sizes'] = Property.objects.order_by('-id')
        return context

class BuyProductView(DetailView):
    model = Product
    template_name = 'buy_confirmation.html'
    context_object_name = 'buying_product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        return context

class BuySizeProductView(DetailView):
    model = Product
    template_name = 'buy_single.html'
    context_object_name = 'buying_size_product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['sizes'] = Property.objects.order_by('-id')
        return context

class HelpView(CreateView):
    template_name = "help.html"
    model = Question
    form_class = AskQuestionForm
    success_url = reverse_lazy('core:help-page')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
