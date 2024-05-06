from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return f'{self.role_name}'