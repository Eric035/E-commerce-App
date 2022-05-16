from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    favorite_team = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    on_sale = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except Exception as err:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=500, null=True)
    delivered = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)
    
    # Get total number of items in cart
    @property
    def get_cart_item_count(self):
        ordered_items = self.orderitem_set.all()
        return sum([item.get_total_price for item in ordered_items])

    # Get total price of items cart
    @property
    def get_cart_total(self):
        ordered_items = self.orderitem_set.all()
        return sum([item.get_total_price for item in ordered_items])


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def get_total_price(self):
        return self.product.price * self.quantity



class Shipment(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=350, null=True)
    city = models.CharField(max_length=350, null=True)
    province = models.CharField(max_length=350, null=True)
    postal_code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.address

    