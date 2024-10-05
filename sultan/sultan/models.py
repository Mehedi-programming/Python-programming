from django.db import models

class ABOUT(models.Model):
    Tittle=models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Name = models.CharField(max_length=250)
    Age =  models.CharField(max_length=520)
    Occupation =  models.CharField(max_length=500)
    Phone =  models.CharField(max_length=500)
    Email =  models.CharField(max_length=500)
    Nationality =  models.CharField(max_length=500)
    S_image=models.ImageField(upload_to='myimages/')

class EDUCATION(models.Model):
    Degree_department = models.CharField(max_length=300)
    Institute = models.CharField(max_length=500)
    Session = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)

class EXPERIENCE(models.Model):
    Position = models.CharField(max_length=250)
    Company_name = models.CharField(max_length=250)
    Time = models.CharField(max_length=250)
    Representation = models.CharField(max_length=250)

class RESARCH(models.Model):
    Resarch_name = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    Time = models.CharField(max_length=250)

class FUNFACT(models.Model):
    Tittle = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Experience_year = models.CharField(max_length=250)
    Client_count = models.CharField(max_length=250)
    Project_count = models.CharField(max_length=250)
    Digital_products = models.CharField(max_length=250)

class SKILL(models.Model):
    Tittle = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    HTML_percantage = models.CharField(max_length=250)
    CSS_percantage = models.CharField(max_length=250)
    Python_percantage = models.CharField(max_length=250)
    JavaScript = models.CharField(max_length=250)
    Research = models.CharField(max_length=500)

class TESTIMONIAL(models.Model):
    Tittle = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Client_name = models.CharField(max_length=250)
    Company_name = models.CharField(max_length=250)
    Articles = models.CharField(max_length=250)
    JavaScript = models.CharField(max_length=250)
    Research = models.CharField(max_length=250)

class SERVICE(models.Model):
    Tittle_1_web = models.CharField(max_length=400)
    Tittle2_security = models.CharField(max_length=500)

class CONTACT(models.Model):
    Tittle = models.CharField(max_length=100)
    Location = models.CharField(max_length=500)
    Phone = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)

class HOMEPAGE(models.Model):
    Name = models.CharField(max_length=100)
    Article = models.CharField(max_length=500)






