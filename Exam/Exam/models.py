from django.db import models

class About(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=300)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    fb=models.CharField(max_length=255)
    github=models.CharField(max_length=255)
    gmail=models.CharField(max_length=255)
    