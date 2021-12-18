from django.shortcuts import render
# Create your views here.
#posts/views.py 
#from django.http import HttpResponse
#Импортируем модель,чтобы обратиться к ней
# from .models import Post

app_name = 'posts_app'

def index(request): 
    context = {
        'title': 'Главная страница',
    }
    template = 'posts/index.html'
    return render(request, template, context)
    # return HttpResponse('Главная страница')


#Страница со списком постов
def group_posts(request,slug):
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
        'text': 'Тут будет сортирока постов по группам',
    }
    template = 'posts/group_posts.html'
    return render(request, template, context)


def group_list(request):
    '''Здесь посты будут отфильтрованы по группам'''
    template='posts/group_list.html'
    return render(request, template)
    #return HttpResponse(f'Заметки по группам')
