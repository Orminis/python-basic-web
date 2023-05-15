from django.core.exceptions import ValidationError
from django.db import models


def validate_name(value):
    first_and_last_name = value.split(' ')
    if len(first_and_last_name) < 2:
        raise ValidationError('Name must include first and last names')


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    def __str__(self):
        return self.name


# model just for fast check
class Person(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(max_length=MAX_NAME_LEN)
    age = models.IntegerField(null=True, blank=True)

    pets = models.ManyToManyField(
        Pet,
        related_name='persons',
    )