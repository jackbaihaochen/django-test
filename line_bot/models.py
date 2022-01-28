from django.db import models

# Create your models here.
class LineAuthInfo(models.Model):
    key = models.CharField(max_length=50)
    value = models.TextField()

    def __str__(self):
        return self.key