from django.db import models

# Create your models here.
class Cloth(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.IntegerField()
    material=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)