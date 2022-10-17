from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __repr__(self):
        return self.title


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    img = models.CharField(max_length=1000, default='')
    sn = models.CharField(max_length=50, default='')
    defects = models.CharField(max_length=2000, default='')
    hazards = models.CharField(max_length=2000, default='')
    consumers = models.CharField(max_length=2000, default='')
    supplier = models.CharField(max_length=2000, default='')
    traders = models.CharField(max_length=2000, default='')
    sold_venues = models.CharField(max_length=1000, default='')
    avaiable_sale_date = models.CharField(max_length=1000, default='')
    content = models.CharField(max_length=2000, default='')
    published_date = models.CharField(max_length=50, default='')
    # created_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ["category"]

    def __repr__(self):
        return f"{self.product_name} - {self.sn} - {self.category}"


class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    product_sn = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __repr__(self):
        return f"{self.name} - {self.phone} - {self.created_date}"
