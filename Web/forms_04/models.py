from django.db import models

# Create your models here.

# model just for fast check
class Person(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(max_length=MAX_NAME_LEN)
    age = models.IntegerField(null=True, blank=True)
