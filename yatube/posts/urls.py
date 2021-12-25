from django.urls import path
from posts import views

app_name = "my_posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group, name='my_group'),
    # path('post/<slug:slug>', views.post_detail),
]
