from django.db import models
from .Detaillesson import Detaillesson
from .Extent import Extent


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    detail_lesson = models.ForeignKey(Detaillesson, models.CASCADE, blank=False, null=False)
    extent = models.ForeignKey(Extent, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return f'''{self.title} - {self.description} - {self.detail_lesson}'''