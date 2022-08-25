from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=50)
    comments = models.CharField(max_length=255)