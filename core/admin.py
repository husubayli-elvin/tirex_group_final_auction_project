from django.contrib import admin
from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property


admin.site.register([User_bids, Category, Brand, Product, Property_name, Property, Product_property])