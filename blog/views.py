from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


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
@require_http_methods(['GET', 'POST'])
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
        context['data']['post_id'] = post.id
        return JsonResponse(context)
    return render(request, "blog-add.html")


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_post(request, pk):
    context = {"status": True,
               "message": "", "data": {}}
    try:
        post = Post.objects.get(pk=pk, author=request.user)
        post.delete()
        post_exists = Post.objects.filter(author=request.user).exists()
        context['data']['post_exists'] = post_exists
        context["message"] = "Post successfully deleted."
        return JsonResponse(context, status=200)
    except Exception as e:
        print(e)
        context["message"] = "Post not found"
        return JsonResponse(context, status=404)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def edit_post(request, pk):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Post.objects.get(pk=pk)
        post.title = title
        post.content = content
        if request.FILES:
            post_image = request.FILES['post-image']
            post.image = post_image
        post.author = request.user
        post.save()
        context = {"status": True,
                   "message": "Post successfully updated.", "data": {}}
        context['data']['post_id'] = post.id
        return JsonResponse(context)
    post = get_object_or_404(Post, pk=pk)
    context['post'] = post
    return render(request, "blog-edit.html", context)
