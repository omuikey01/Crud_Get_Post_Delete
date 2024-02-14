from django.db import models

# Create your models here.

class ProductEntry(models.Model):
    user_from = models.CharField(max_length=100)
    user_to = models.CharField(max_length=100)
    km = models.IntegerField()
    price = models.IntegerField()
    