from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import django_filters


choicesbrand = (
        ('Whiskas', 'Whiskas'),
        ('Natura Pet Products', 'Natura Pet Products'),
        ('Champion Petfoods', 'Champion Petfoods'),
        ('Golden Eagle HH', 'Golden Eagle HH'),
        ('Bosch Tiernahrung', 'Bosch Tiernahrung'),
        ("Hill's Pet Nutrition", "Hill's Pet Nutrition"),
        ('ROYAL CANIN', 'ROYAL CANIN'),
        ('Nestle Purina', 'Nestle Purina'),
)
choicesanimal = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Fish', 'Fish'),
        ('Bird', 'Bird'),
        ('Reptile', 'Reptile'),
        ('Hamster', 'Hamster'),
        ('Other', 'Other'),
)
choicesclass = (
        ('Food', 'Food'),
        ('Nutrient', 'Nutrient'),
        ('Toy', 'Toy'),
        ('Accessories', 'Accessories')
)


class Brand(models.Model):

    name = models.CharField('brand of the product', max_length=50, choices=choicesbrand)

    class Meta:
        verbose_name_plural = "brands"

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField('animal species of the product', max_length=50, choices=choicesanimal)

    class Meta:
        verbose_name_plural = "animals"

    def __str__(self):
        return self.name


class Classification(models.Model):
    name = models.CharField('type of product', max_length=50, choices=choicesclass)

    class Meta:
        verbose_name_plural = "classifications"

    def __str__(self):
        return self.name


class Product(models.Model):
    choicesavail = (
        ('Yes', 'Yes'),
        ('In other city', 'In other city'),
        ('Expected', 'Expected'),
    )

    name = models.CharField('name of product', max_length=50)
    image = models.ImageField('url for picture of product', null=True, blank=True)
    description = models.TextField('description of product')
    rating = models.IntegerField('rating', default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    price = models.IntegerField('price', default=0, validators=[MinValueValidator(0)])
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    availability = models.CharField('availability of product', max_length=20, choices=choicesavail)
    novelty = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class ProductFilter(django_filters.FilterSet):
    choiceprices = (
        (100, 100),
        (500, 500),
        (1000, 1000),
        (1500, 1500),
        (2000, 2000),
        (4000, 4000),
    )
    choicesrating = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    )
    choicesavail = (
        ('Yes', 'Yes'),
        ('In other city', 'In other city'),
        ('Expected', 'Expected'),
    )

    name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.NumberFilter()
    price__gt = django_filters.ChoiceFilter(field_name='price', lookup_expr='gte', choices=choiceprices)
    price__lt = django_filters.ChoiceFilter(field_name='price', lookup_expr='lte', choices=choiceprices)
    rating = django_filters.ChoiceFilter(field_name='rating', choices=choicesrating)
    brand = django_filters.ChoiceFilter(field_name='brand', choices=choicesbrand)
    animal = django_filters.ChoiceFilter(field_name='animal', choices=choicesanimal)
    classification = django_filters.ChoiceFilter(field_name='classification', choices=choicesclass)
    availability = django_filters.ChoiceFilter(field_name='availability', choices=choicesavail)

    class Meta:
        model = Product
        exclude = ['image', 'description', 'novelty']


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    image = models.ImageField('url for picture', null=True, upload_to="images/", blank=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.user.username)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    rating = models.IntegerField('rating', default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return '%s - %s - %s' % (self.id, self.product.name, self.username)

