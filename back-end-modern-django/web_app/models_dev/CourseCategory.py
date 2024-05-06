from django.db import models
from .Category import Category
from .Course import Course


class CourseCategory(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(Category, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    class Meta:
        db_table = 'course_category'

    def __str__(self):
        return f'{self.course} - {self.category}'
    
    def save(self, *args, **kwargs):
        super(CourseCategory, self).save(*args, **kwargs)