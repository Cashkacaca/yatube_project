from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # # Страницы сообществ
    path('group/<slug:slug>/', views.group_posts),
    # Добавляем страницу group_list.html
    # path('group_list/', views.grou_list_views),
]
