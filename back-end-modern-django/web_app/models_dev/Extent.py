from django.db import models


class Extent(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'extent'

    def __str__(self):
        return f'{self.name}'