from django.db import models
from .Exercise import Exercise
from .User import User

class Submission(models.Model):
    code = models.TextField(blank=False, null=False)
    exercise = models.ForeignKey(Exercise, models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'submission'

    def __str__(self):
        return f'''{self.code} - {self.exercise} - {self.user}'''