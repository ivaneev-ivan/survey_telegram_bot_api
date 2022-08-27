from django.db import models


class Question(models.Model):
    title = models.CharField('Текст вопроса', max_length=255)
    answer = models.TextField('Ответ на вопрос')
    user_id = models.IntegerField('Id пользователя телеграм')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        db_table = 'questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
