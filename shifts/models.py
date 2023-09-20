from django.db import models

# Create your models here.
class Shift(models.Model):
    name = models.Charfield(max_length=200)
    position = models.Charfield(max_length=200)
    date = models.Charfield(max_length=200)
    start_time = models.Charfield(max_length=200)
    end_time = models.Charfield(max_length=200)