from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductFilterSerializer
from core.models import Product
from rest_framework.response import Response

class SearchProductAPI(ListAPIView):
    serializer_class = ProductFilterSerializer

    def get_queryset(self):
        title = self.request.data.get('title')
        category = self.request.data.get('category')
        brand = self.request.data.get('brand')
        size_type = self.request.data.get('size_type')
        price_list = self.request.data.get('price')
        release_year = self.request.data.get('years')
        print(release_year)
        queryset = Product.objects.order_by('-id')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__title=category)
        if brand:
            queryset = queryset.filter(brand__title=brand)
        if size_type:
            queryset = queryset.filter(made_for__in=size_type)
        if price_list:
            for price in price_list:
                # print(price)
                queryset = queryset.filter(current_price__range=(price[0], price[1]))
        if release_year:
            queryset = queryset.filter(release_date__in=release_year)

        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)