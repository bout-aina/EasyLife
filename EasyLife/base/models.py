from django.db import models

# Create your models here.
class Contact_us(models.Model):
    nom=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    sujet=models.CharField(max_length=30)
    Message=models.CharField(max_length=30)