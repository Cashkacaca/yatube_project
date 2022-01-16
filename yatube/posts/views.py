# from django.http import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


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
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    template_group_list = 'posts/group_list.html'

    title = 'Здесь будет информация о группах проекта Yatube'

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template_group_list, context)


# Болше не нужно
# def group_posts(reques, slug):
    # return HttpResponse('Сообщества (группы) социальной сети YaTube {slug}.')

# Create your views here.
