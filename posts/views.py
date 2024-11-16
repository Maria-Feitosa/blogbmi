from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'poster_url', 'detail']
    template_name = 'posts/create.html'
    
    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})

class PostUpateView(generic.UpdateView):
    model = Post
    fields = ['name', 'poster_url', 'detail']
    template_name = 'posts/update.html'

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')
