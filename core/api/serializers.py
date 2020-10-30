from rest_framework import serializers
from core.models import Product

class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =('title', 'made_for', 'image', 'retail_price', 'current_price', 'description', 'condition', 'delivery_fee', 'brand', 'owner', 'added_at', 'updated_at')