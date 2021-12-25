from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('posts.urls', namespace="my_posts")),
    path('admin/', admin.site.urls),
]
