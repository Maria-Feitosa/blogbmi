from django.forms import ModelForm
from .models import Post, Comment
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "poster_url",
            "categoria",
            "detail",
        ]
        labels = {
            "name": "Título",
            "poster_url": "URL do Poster",
            "detail": "Detalhes",
        }

class CommentForm(ModelForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = ["author",
                  "post",
                  "comentario",
        ]
        labels = {
            'author': 'Seu nome',
            'post': 'post que quer comentar',
            "comentario": "Deixe seu comentário"
        }