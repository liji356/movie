from django.db import models

class MovieList(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    Year=models.IntegerField()
    image=models.ImageField(upload_to='pics')


    def __str__(self):
        return self.name


# Create your models here.
