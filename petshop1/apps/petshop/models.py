from django.db import models

class product(models.Model):
    name = models.CharField('name of product', max_length = 50)
    pic_url = models.CharField('url for picture of product', max_length = 200)
    description = models.CharField('description of product', max_length = 200)
    rating = models.IntegerField('rating', default=0)
    price = models.IntegerField('price', default=0)

    class Meta:
        verbose_name_plural = "products"
    def __str__(self):
        return self.name
