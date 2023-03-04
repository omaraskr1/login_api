from django.db import models

# Create your models here.
class awsimage(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField('images/',default="")

# class test(models.Model):
#     title=models.CharField(max_length=50)

