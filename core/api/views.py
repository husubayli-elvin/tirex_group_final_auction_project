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
        print(self.request.data)
        print(size_type)
        queryset = Product.objects.all()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__title=category)
        if brand:
            queryset = queryset.filter(brand__title=brand)
        if size_type:
            queryset = queryset.filter(made_for__in=size_type)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)