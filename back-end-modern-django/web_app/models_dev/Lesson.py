from django.db import models
from .Course import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, models.CASCADE, blank=True, null=True)

    
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return f'''{self.title} - {self.description} - {self.course}'''