from django.urls import path
from blog.views import blogs_view

urlpatterns = [
    path("", blogs_view)
]
