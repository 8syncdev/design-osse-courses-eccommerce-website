from django.db import models
from .Course import Course
from .Status import Status

class CourseStatus(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, blank=False, null=False)
    status = models.ForeignKey(Status, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'course_status'
        unique_together = ('course', 'status')

    def __str__(self):
        return f'''{self.course} - {self.status}'''