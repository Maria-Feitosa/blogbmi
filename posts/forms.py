from django.forms import ModelForm
from .models import Post, Comment
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "poster_url",
            "detail",
        ]
        labels = {
            "name": "Título",
            "poster_url": "URL do Poster",
            "detail": "Detalhes",
        }

class CommentForm(ModelForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput)
    
    class Meta:
        model = Comment
        fields = [
            "comentario",
        ]
        labels = {
            "comentario": "Deixe seu comentário"
        }