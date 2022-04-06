from django.db import models

# Create your models here./
class Citoyen(models.Model):
    infoId = models.CharField(max_length=500,primary_key=True)
    numcin = models.CharField(max_length=500)
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    tel = models.CharField(max_length=500)
    infraction = models.CharField(max_length=500)



