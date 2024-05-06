from django.db import models
from .Category import Category
from .User import User
from .Discount import Discount
from .Extent import Extent



class Course(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField()
    instructor = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    discount = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True)
    extent = models.ForeignKey(Extent, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return f'''{self.title} - {self.price} - {self.instructor}'''
    
    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)