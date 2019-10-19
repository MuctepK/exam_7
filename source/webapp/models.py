from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=256, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.question[:30]


class Choice(models.Model):
    answer = models.TextField(max_length=128, verbose_name='Ответ')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.answer[:30]
