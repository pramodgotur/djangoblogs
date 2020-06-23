from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blogs_view(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, "home.html", context)


def blog_detail_view(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk)
    context['post'] = post
    return render(request, "blog-detail.html", context)
