from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField('name of product', max_length = 50)
    pic_url = models.CharField('url for picture of product', max_length = 200)
    description = models.CharField('description of product', max_length = 200)
    rating = models.IntegerField('rating', default=0, validators = [MaxValueValidator(5), MinValueValidator(0)])
    price = models.IntegerField('price', default=0, validators = [MinValueValidator(0)])

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     user_id = user.id;
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return  self.name
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200, null=True)
#     city = models.CharField(max_length=200, null=True)
#     state = models.CharField(max_length=200, null=True)
#     zipcode = models.CharField(max_length=200, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.address
