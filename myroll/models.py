from django.conf import settings
from django.db import models
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    total_number = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    charge = models.CharField(max_length=10)

    def assignment(self):
        self.total_number += 1
        self.save()

    def __str__(self):
        return self.name
