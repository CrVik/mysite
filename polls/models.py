from django.db import models

class Question(models.Model):
    question_text = models.CharField('Текст вопроса', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')
    create_date = models.DateTimeField('Время создания вопроса', auto_now_add=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('Ответ на вопрос', max_length=200)
    votes = models.IntegerField('Количесвто ответов', default=0)
    def __str__(self):
        return self.choice_text




