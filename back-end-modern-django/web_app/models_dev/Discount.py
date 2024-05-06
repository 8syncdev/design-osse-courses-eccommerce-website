from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Discount(models.Model):
    discount_percentage = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], 
        max_digits=5, decimal_places=2, blank=False, null=False,
        default=0.0
    )
    code_name = models.CharField(max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return f'{self.course.title} - {self.discount_percentage}%'