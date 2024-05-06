from django.db import models
from .Shoppingcart import Shoppingcart




class Invoice(models.Model):
    tolal_price = models.DecimalField(max_digits=30, decimal_places=20, blank=False, null=False)
    shopping_cart = models.ForeignKey(Shoppingcart, on_delete=models.CASCADE, blank=False, null=False)
    
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return f'''{self.total_amount} - {self.user}'''