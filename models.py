from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    brand =  models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
