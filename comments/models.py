from django.db import models
from django.utils import timezone

from clients.models import Client


class Comments(models.Model):
    author = models.ForeignKey(
        to = Client,
        verbose_name = 'Автор',
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'client_comments',
    )
    text = models.CharField(
        verbose_name = 'Текст комментария',
        max_length = 150,
    )
    likes = models.PositiveBigIntegerField(
        verbose_name = 'Лайки',
        default = 0,
    )
    dislikes = models.PositiveBigIntegerField(
        verbose_name = 'Дизлайки',
        default = 0,
    )
    date_comment = models.DateTimeField(
        verbose_name = 'Дата комментирования',
        default = timezone.now,
    )
    reply_comment = models.ForeignKey(
        verbose_name = 'Ответы на комментарии',
        to = 'self',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name='replies',
    )