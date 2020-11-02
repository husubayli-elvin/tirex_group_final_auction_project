from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductFilterSerializer
from core.models import Product

class SearchProductAPI(ListAPIView):
    serializer_class = ProductFilterSerializer

    def get_queryset(self):
        title = self.request.data['title']
        category = self.request.data['category']
        print(title)
        queryset = Product.objects.all()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(brand__category__title=category)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)