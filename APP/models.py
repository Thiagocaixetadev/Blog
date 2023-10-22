from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Racunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    corpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')
    
    class Meta:
        ordering = ('-publicado',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.titulo
