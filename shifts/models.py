from django.db import models

# Create your models here.
class Shift(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)