from django.db import models

# Create your models here.
class mywebsitedb(models.Model):
    email = models.CharField(max_length=75)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)

