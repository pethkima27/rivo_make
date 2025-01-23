from django.db import models

class Card(models.Model):
    foto = models.URLField()
    nome = models.CharField(max_length=50)
    defesa = models.IntegerField()
    ataque = models.IntegerField()
    hp = models.IntegerField()
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
