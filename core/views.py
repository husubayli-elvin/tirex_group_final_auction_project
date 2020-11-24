from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property, Question
from .forms import AskQuestionForm, ProductTransactionForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import firebase_admin
from firebase_admin import db, credentials


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sneakers'] = [i for i in Product.objects.order_by('-id') if i.category.title == "Sneakers"][:5]
        context['release_calendar_products'] = [i for i in Product.objects.order_by('-id') if i.category.title == "Sneakers"][:4]
        return context


class StreetwearView(TemplateView):
    template_name = 'streetwear.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streetwear'] = [i for i in Product.objects.order_by('-id') if i.category.title == "Wear"][:5]
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
        context['same_brand'] = Product.objects.filter(brand__title=product.brand.title)
        context['sizes'] = Property.objects.order_by('-id')
        context['highest_bid'] = [i for i in User_bids.objects.filter(product=product).order_by('price') if i.is_sell == False][:1]
        context['lowest_ask'] = [i for i in User_bids.objects.filter(product=product).order_by('-price') if i.is_sell == True][:1]
        return context


class SellProductView(LoginRequiredMixin, FormMixin, DetailView):
    model = Product
    template_name = 'sell_confirmation.html'
    form_class = ProductTransactionForm
    context_object_name = 'selling_product_detail'
    

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = ProductTransactionForm(initial={'price': product.current_price})
        context['highest_bid'] = [i for i in User_bids.objects.filter(product=product).order_by('price') if i.is_sell == False][:1]
        context['lowest_ask'] = [i for i in User_bids.objects.filter(product=product).order_by('-price') if i.is_sell == True][:1]
        return context

    def get_success_url(self):
        return reverse_lazy('core:product-detail', kwargs={'slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not firebase_admin._apps:
            cred = credentials.Certificate(settings.FIREBASE_CONF_FILE)
            default_app = firebase_admin.initialize_app(cred, {'databaseURL': settings.FIREBASE_DATABASE_URL})
        ref = db.reference('')
        if form.is_valid():
            prices_ref = ref.child(f'sell/{self.get_object().pk}')
            prices_ref.update({
                'price': float(form.instance.price)
            })
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_sell = True
        form.instance.product = self.get_object()
        print(form.instance.price)
        form.save()
        return super().form_valid(form)

class BuyProductView(DetailView):
    model = Product
    template_name = 'buy_confirmation.html'
    context_object_name = 'buying_product_detail'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        return context

class HelpView(CreateView):
    template_name = "help.html"
    model = Question
    form_class = AskQuestionForm
    success_url = reverse_lazy('core:help-page')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
