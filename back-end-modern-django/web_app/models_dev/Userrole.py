from django.db import models
from .User import User
from .Role import Role

class Userrole(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    role = models.ForeignKey(Role, models.CASCADE, blank=False, null=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'userrole'

    def __str__(self):
        return f'''{self.user} - {self.role}'''