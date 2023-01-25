from django.db import models
from django.conf import settings
from decimal import Decimal

from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    address1 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    total_paid = models.FloatField()
    order_key = models.CharField(max_length=100, null=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
