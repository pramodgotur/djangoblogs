from django.urls import path
from blog.views import blogs_view, blog_detail_view, add_post, my_posts, delete_post

urlpatterns = [
    path("", blogs_view),
    path("blog-detail/<int:pk>/", blog_detail_view),
    path("add-post/", add_post),
    path("my-posts/", my_posts),
    path("delete-post/<int:pk>/", delete_post),
]
