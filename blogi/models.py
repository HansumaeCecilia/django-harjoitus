from django.db import models

# Create your models here.
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    ingressi = models.TextField(max_length=5000, blank=True)
    teksti = models.TextField()
    kuva = models.ImageField(upload_to='blogi/kuvat', null=True, blank=True)
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.otsikko
    
    def luo_ingressi(self):
        if self.ingressi:
            return self.ingressi
        return self.teksti[:50] + '...'