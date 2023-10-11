from django.contrib.auth.models import User
from django.db import models

class Producs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    archieved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Product (pk={self.pk}, name={self.name!r})"
    
class Order(models.Model):
    delivery_adress = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Producs, related_name="orders")