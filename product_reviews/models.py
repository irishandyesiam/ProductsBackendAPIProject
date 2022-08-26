from django.db import models
from models import Product

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=50)
    comments = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL)