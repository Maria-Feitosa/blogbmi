from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('update/<int:pk>/', views.PostUpateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/comentario/',views.CommentCreateView.as_view(), name='comentario')
]