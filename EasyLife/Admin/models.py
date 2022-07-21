from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    email=models.CharField(max_length=30)
    mdp=models.CharField(max_length=30)