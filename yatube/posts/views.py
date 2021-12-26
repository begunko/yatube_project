from django.shortcuts import get_object_or_404, render
from posts.models import Group, Post

POSTS_PER_PAGE: int = 10


def index(request):
    latest = Post.objects.all()[:POSTS_PER_PAGE]
    return render(request, 'posts/index.html', {'posts': latest})


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    return render(request, 'group.html', {'group': group, 'posts': posts})
