# posts/urls.py

from django.urls import path
from . import views

app_name='all_posts'

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('groupe/<slug:slug>/', views.group_posts),
    path('group_list', views.group_list),
]