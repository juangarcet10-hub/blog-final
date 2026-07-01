from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo