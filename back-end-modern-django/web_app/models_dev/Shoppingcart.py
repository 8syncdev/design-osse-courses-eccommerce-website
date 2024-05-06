from django.db import models
from .User import User


class Shoppingcart(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    tolal_price = models.DecimalField(max_digits=30, decimal_places=20, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'shoppingcart'

    def __str__(self):
        return f'''{self.user}'''