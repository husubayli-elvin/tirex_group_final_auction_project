
from rest_framework import serializers
from core.models import Product

class ProductFilterSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =('id','title', 'made_for', 'image', 'retail_price', 'current_price', 'description', 'condition', 'delivery_fee', 'brand', 'owner', 'added_at', 'updated_at', 'url',)
    
    def get_url(self, product):
        return product.get_absolute_url()