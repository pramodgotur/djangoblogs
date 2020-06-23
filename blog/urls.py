from django.urls import path
from blog.views import blogs_view, blog_detail_view

urlpatterns = [
    path("", blogs_view),
    path("blog-detail/<int:pk>/", blog_detail_view),
]
