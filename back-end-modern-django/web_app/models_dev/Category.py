from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'''{self.category_name}'''
    
    def save(self, *args, **kwargs):
        self.category_name = self.category_name.title()
        # if self.created_at is None:
        #     self.created_at = timezone.now()
        # self.updated_at = timezone.now()
        super(Category, self).save(*args, **kwargs)