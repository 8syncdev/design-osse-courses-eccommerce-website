from django.db import models
from .User import User
from .Course import Course


class Enrollment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, models.CASCADE, blank=False, null=False)


    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return f'''{self.user} - {self.course}'''