from django.forms import ModelForm
from .models import Post


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