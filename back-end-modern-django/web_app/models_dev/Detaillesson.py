from django.db import models
from .Lesson import Lesson
from .Extent import Extent

class Detaillesson(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    lesson = models.ForeignKey(Lesson, models.CASCADE, blank=False, null=False)
    extent = models.ForeignKey(Extent, models.CASCADE, blank=False, null=False)
    
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'detaillesson'

    def __str__(self):
        return f'''Tên: {self.name}, Bài Học: {self.lesson}, Mức độ: {self.extent}'''