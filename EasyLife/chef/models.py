from django.db import models


class Chef(models.Model):
    id = models.AutoField(primary_key=True)
    email=models.CharField(max_length=30)
    mdp=models.CharField(max_length=30)
# Create your models here.
