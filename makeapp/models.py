from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    foto = models.ImageField(upload_to='user', blank=True, null=True, default='user/default_image.webp')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Produto(models.Model):
    foto = models.ImageField(upload_to='', blank=True, null=True)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.titulo
