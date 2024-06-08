from django.db import models

class Bug(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bugs/')
    points = models.IntegerField()
