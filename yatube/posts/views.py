from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(reguest):
    return HttpResponse('Список постов')


def post_detail(reguest, slug):
    return HttpResponse(f'Тут что то про пост пото поеняю {slug}')