from django.db import models
from django.contrib.auth import get_user_model

from django.db.models import Sum


from products.models import Product
# Create your models here.

User = get_user_model()

class Order(models.Model):
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.items.aggregate(total_price=Sum('price'))['total_price']

    
    def __str__(self):
        return str(self.user)
