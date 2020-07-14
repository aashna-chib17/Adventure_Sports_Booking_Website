from django.db import models
from datetime import datetime

class event(models.Model):
    title = models.CharField(max_length=200)
    city =  models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_open =  models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

