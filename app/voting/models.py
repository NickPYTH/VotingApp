from django.db import models
import datetime
from django.contrib import admin




class Список_вопросов(models.Model):
    question_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.question_text
 
class Список_ответов(models.Model):
    unique_key = models.IntegerField(unique=True)
    Вопрос = models.TextField()
    Оценка = models.IntegerField()
    Комментарий = models.TextField(blank=True)
    Дата = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.unique_key) + " " + str(self.Дата) + " " +  str(self.Вопрос)

class Список_ПВИ(models.Model):
    Название_ПВИ = models.CharField(max_length=200)
    Местонахождение_ПВИ = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Название_ПВИ)

class Дата_окончания_голосования(models.Model):
    Дата = models.DateField()

    def __str__(self):
        return str(self.Дата)

class Общие_комментарии(models.Model):
    unique_key = models.IntegerField(unique=True)
    Пожелание = models.TextField()

    def __str__(self):
        return str(self.unique_key)