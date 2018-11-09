from django.db import models

class Artigo(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()


    class Meta:
         ordering = ('created',)
