from django.db import models
from django.conf import settings

class Category(models.Model):
    categoria = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.categoria}'
    

class Post(models.Model):
    categoria = models.ManyToManyField(Category)
    name = models.CharField(max_length=255)
    poster_url = models.URLField(null=True)
    detail = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} Criado em: {self.data_postagem}'


    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()

    def __str__(self):
        return f'{self.author.username} referente a {self.post}'

