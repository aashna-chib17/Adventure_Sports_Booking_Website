from django.db import models

class booking(models.Model):
    user_id = models.IntegerField()
    event_id =  models.IntegerField()
    event_title = models.TextField(max_length=200)
    name=models.TextField(max_length=200)
    email=models.EmailField(max_length=200)
    ticket = models.IntegerField()
    phone= models.TextField(max_length=200)
    date= models.DateField()

    def __str__(self):
        return self.event_title




