from django.db import models

from django.urls import reverse

# Create your models here.

class Technicien(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mdp=models.CharField(max_length=30)
    tel=models.CharField(max_length=10)
    ville=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)
    domaine=models.CharField(max_length=30)
    diplome=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom + " "+self.prenom
        
    def get_absolute_url(self):
        return reverse("profile",kwargs={"id": self.id})
        #return f"/technicien/profile/"