from django.db import models
from django.conf import settings

class Post(models.Model):
    name = models.CharField(max_length=255)
    poster_url = models.URLField(null=True)
    detail = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} Criado em: {self.data_postagem}'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    comentarios = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'