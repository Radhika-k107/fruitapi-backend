from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=15)
    colour = models.CharField(max_length=15)
    calories = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name