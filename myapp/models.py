from django.db import models

# Create your models here.

class Registration(models.Model):

    Name = models.CharField(max_length=25)
    Mobile_No = models.IntegerField()
    Area = models.CharField(max_length=25)
    Postal = models.IntegerField()
    State = models.CharField(max_length=15)
