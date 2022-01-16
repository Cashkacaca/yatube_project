# from django.http import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Это главная страница проекта Yatube'
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        'posts': posts,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        # 'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
    # Больше не нужна нижняя строчка после добавления стр. 8 и 9
    # return HttpResponse('Главная страница социальной сети YaTube.')


# Добавил страницу posts/group_list.html
def group_posts(request, slug):
    template_group_list = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        # 'posts': posts,
    }
    return render(request, template_group_list, context)


# Болше не нужно
# def group_posts(reques, slug):
    # return HttpResponse('Сообщества (группы) социальной сети YaTube {slug}.')

# Create your views here.
