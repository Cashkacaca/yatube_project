# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница социальной сети YaTube.')


def group_posts(reques, slug):
    return HttpResponse('Сообщества (группы) социальной сети YaTube {slug}.')

# Create your views here.
