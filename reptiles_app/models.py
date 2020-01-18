from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Reptile(models.Model):
    nom = models.CharField(max_length=100)
    nomEspece = models.CharField(max_length=200)
    ordre = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    poids = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

