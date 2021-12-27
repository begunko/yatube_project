from django.urls import path
from posts import views

app_name = "my_posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # path('post/<slug:slug>', views.post_detail),
]
