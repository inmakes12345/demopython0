from django.db import models

class Movie(models.Model):


    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    movie=models.TextField()

def __str__(self):
    return self.name
