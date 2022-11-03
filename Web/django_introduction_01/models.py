from django.db import models

# Create your models here.


# Maps to a DB Model
class Intro(models.Model):
    # varchar(30), NOT NULL
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    priority = models.IntegerField()
