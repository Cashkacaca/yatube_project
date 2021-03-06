from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    # Тип: CharField (строка с ограничением длины)
    title = models.CharField(max_length=200)
    # типы поля (unique=True) - уникальный адрес группы
    slug = models.SlugField(unique=True)
    description = models.TextField()

    # метод __str__,
    # чтобы при печати объекта модели Group выводилось поле title
    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    #  при добавлении новой записи можно было сослаться на сообщество
    # (на модель Group)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )


# Create your models here.
