from django.contrib import admin
from core.models import User_bids, Category, Brand, Product, Property_name, Property, Product_property, Question, Order
from django.contrib.auth.models import Group

admin.site.site_header = "Compass"
admin.site.index_title = "Compass"
admin.site.site_title = "Compass Administration"


admin.site.register([User_bids, Category, Brand, Product, Property_name, Property, Product_property, Question, Order])
admin.site.unregister(Group)