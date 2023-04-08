from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, null=False)    # will contain the type of activity i.e. plane,train,utility,et.t.c. 
    distance = models.IntegerField(default=None)
    milage = models.IntegerField(default=None)
    electricity_consumption = models.IntegerField(default = None)
    gass_volume = models.IntegerField(default= None)
    emission_factor = models.IntegerField(default=None, null=False)
    carbon_footprint = models.IntegerField(default=None, null=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carbon_footprint = models.IntegerField(default= 0) 
    carbon_footprint = models.IntegerField(default= 0)
    