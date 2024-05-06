from django.db import models
from .Shoppingcart import Shoppingcart
from .Course import Course


class ShoppingcartDetails(models.Model):
    shopping_cart = models.ForeignKey(Shoppingcart, models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, models.CASCADE, blank=False, null=False)


    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'shoppingcartDetails'
        unique_together = (('shopping_cart', 'course'),)

    def __str__(self):
        return f'''{self.shopping_cart} - {self.course}'''