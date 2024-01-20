from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    sulg=models.SlugField(unique=True)
    desc=models.TextField(max_length=10000)
    descp=models.TextField(default="Tell you though about it",max_length=1000000)
