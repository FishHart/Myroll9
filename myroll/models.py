from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone


class Attending(models.Model):
    userpk = models.IntegerField(unique=True, primary_key=True)
    subject = models.CharField(max_length=10)

    # def assignment(self):
    #     self.total_number += 1
    #     self.save()

    def __str__(self):
        return self.subject

class Subject(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    total = models.IntegerField()
    count = models.IntegerField()
    
