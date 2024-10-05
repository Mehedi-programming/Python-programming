from django.db import models

class ABOUT(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=500)
    Occupation = models.CharField(max_length=250)
    Phone =  models.CharField(max_length=520)
    Email =  models.CharField(max_length=500)
    Nationality =  models.CharField(max_length=500)

class Education(models.Model):
    Degree = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Institute = models.CharField(max_length=250)
    Session = models.CharField(max_length=250)
    Result = models.CharField(max_length=250)

