from django.db import models
from .User import User
from .Crypto import Crypto

class WalletCrypto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=20, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'wallet_crypto'

    def __str__(self):
        return f'''{self.user} - {self.crypto_name} - {self.amount}'''

    def save(self, *args, **kwargs):
        super(WalletCrypto, self).save(*args, **kwargs)
