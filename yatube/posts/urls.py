# posts/urls.py

from django.urls import path
from . import views

app_name='all_posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('group_posts', views.group_posts, name='group_posts'),
    path('group_posts.html', views.group_posts, name='group_posts'),
    path('group_list', views.group_list, name='group_list'), 
    path('group_list.html', views.group_list, name='group_list'),
]