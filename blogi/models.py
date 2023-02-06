from django.db import models

# Create your models here.
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()