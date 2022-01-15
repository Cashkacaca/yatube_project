from django.urls import path
from . import views
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='master_page'),
    # # Страницы сообществ
    path('group/<slug:slug>/', views.group_posts, name='all_group_records',),
]
