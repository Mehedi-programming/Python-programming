from django.db import models
 class About(models.Model):
    contuct=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    fb=models.CharField(max_length=500) 
    phone=models.CharField(max_length=500)
    git=models.CharField(max_length=500)
    