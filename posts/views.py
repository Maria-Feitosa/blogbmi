from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all().order_by('-data_comentario')
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

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comentario.html'
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment.post = post
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})
    
class CategoryListView(generic.ListView):
    model = Category
    template_name = 'posts/categoria.html'

class CategoriaindividualListView(generic.ListView):
    model = Post
    template_name = 'posts/categoria_individual.html'
    
    def get_queryset(self):
        categoria_id = self.kwargs['id']
        return Post.objects.filter(categoria__id=categoria_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs['id']
        categoria = Category.objects.get(id=categoria_id)
        context['categoria'] = categoria
        return context