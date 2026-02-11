from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    search_view,
    posts_by_tag,
    add_comment
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('register/', register_view, name='register'),
    path('posts/<int:pk>/comments/new/', add_comment, name='add_comment'),

    path('search/', search_view, name='search'),
    path('tags/<str:tag_name>/', posts_by_tag, name='tag_posts'),
]
