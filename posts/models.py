from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.usuario.username