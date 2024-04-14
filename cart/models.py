from django.db import models
from django.contrib.auth.models import User
from products.models import Products
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'