from django.db import models
from .Invoice import Invoice
from .ShoppingcartDetails import ShoppingcartDetails



class Invoicedetails(models.Model):
    invoice = models.OneToOneField(Invoice, models.CASCADE, primary_key=True)  
    shopping_cart_details = models.ForeignKey(ShoppingcartDetails, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'invoicedetails'

    def __str__(self):
        return f'''{self.invoice} - {self.course.title}'''