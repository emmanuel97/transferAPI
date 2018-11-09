from django.db import models

class Praia(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    endereco = models.TextField()
    descricao = models.TextField()
    image= models.ImageField(blank=True, null=True)
    rank=models.FloatField(blank=True,default=0)
