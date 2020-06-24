from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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


def my_posts(request):
    context = {}
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    context['posts'] = posts
    return render(request, "my-posts.html", context)


@csrf_exempt
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post_image = request.FILES['post-image']
        post = Post()
        post.title = title
        post.content = content
        post.image = post_image
        post.author = request.user
        post.save()
        context = {"status": True,
                   "message": "Post successfully added.", "data": {}}
        return JsonResponse(context)
    return render(request, "blog-add.html")
