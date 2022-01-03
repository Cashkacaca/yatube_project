# from django.shortcuts import render
# from django.http import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)
    # Больше не нужна нижняя строчка после добавления стр. 8 и 9
    # return HttpResponse('Главная страница социальной сети YaTube.')


# Добавил страницу posts/group_list.html
def group_posts(request, slug):
    template_group_list = 'posts/group_list.html'
    return render(request, template_group_list)


# Болше не нужно
# def group_posts(reques, slug):
    # return HttpResponse('Сообщества (группы) социальной сети YaTube {slug}.')

# Create your views here.
