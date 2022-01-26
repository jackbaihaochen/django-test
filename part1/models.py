from django.db import models

# Create your models here.
class Food(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()