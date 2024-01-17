# models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    is_enabled = models.BooleanField(default=False)
def __str__(self):
    return self.name or ''