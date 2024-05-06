from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=100,null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'''{self.username} - {self.email} - {self.full_name} - {self.phone}'''
    
    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        super(User, self).save(*args, **kwargs)
