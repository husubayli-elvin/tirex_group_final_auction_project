from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductFilterSerializer
from core.models import Product

class SearchProductAPI(ListAPIView):
    serializer_class = ProductFilterSerializer

    def get_queryset(self):
        title = self.request.data['title']
        category = self.request.data['category']
        brand = self.request.data['brand']
        size_type = self.request.data['size_type']
        print(brand)
        queryset = Product.objects.all()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__title=category)
        if brand:
            queryset = queryset.filter(brand__title=brand)
        if size_type:
            queryset = queryset.filter(made_for=size_type)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)