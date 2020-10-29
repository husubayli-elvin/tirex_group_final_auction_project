from django.db import models
from accounts.models import User


class User_bids(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='user_bid')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, db_index=True, related_name='user_bid')

    class Meta:
        verbose_name = 'User Bid'
        verbose_name_plural = 'User Bids'

    def __str__(self):
        return f'{self.user.username}: {self.price}'

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return f'{self.title}'

class Brand(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='brand')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return f'{self.title}'

class Product(models.Model):
    title = models.CharField(max_length=50)
    made_for =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=3000)
    condition = models.CharField(max_length=50)
    delivery_fee = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, db_index=True, related_name='product')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='product')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.title}'

    def save(self):
        super(Product, self).save()
        if not self.current_price:
            self.current_price = self.retail_price
            super(Product, self).save()
            

class Property_name(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='property_name')

    class Meta:
        verbose_name = 'Property Name'
        verbose_name_plural = 'Property Names'

    def __str__(self):
        return f'{self.title}'

class Property(models.Model):
    value = models.CharField(max_length=50)
    property_name = models.ForeignKey('Property_name', on_delete=models.CASCADE, db_index=True, related_name='property')

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return f'{self.value}'

class Product_property(models.Model):
    in_stock = models.BinaryField()
    property = models.ForeignKey('Property', on_delete=models.CASCADE, db_index=True, related_name='product_property')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, db_index=True, related_name='product_property')
