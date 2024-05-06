from django.db import models
from .Shoppingcart import Shoppingcart
from .WalletCrypto import WalletCrypto


class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('paid', 'paid'),
        ('failed', 'failed'),
    )

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    shopping_cart = models.ForeignKey(Shoppingcart, models.CASCADE, blank=False, null=False)
    wallet_crypto = models.ForeignKey(WalletCrypto, models.CASCADE, blank=False, null=False)



    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f'''{self.amount} - {self.status} - {self.shopping_cart}'''