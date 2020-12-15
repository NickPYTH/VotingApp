from django.db import models
import datetime
from django.contrib import admin




class Список_вопросов(models.Model):
    question_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Список_вопросов"
        verbose_name_plural = "Список_вопросов"
 
class Список_ответов(models.Model):
    unique_key = models.IntegerField()
    Вопрос = models.TextField()
    Оценка = models.IntegerField()
    Комментарий = models.TextField(blank=True)
    Дата = models.DateField(auto_now=True)
    ПВИ = models.CharField(max_length=30)

    def __str__(self):
        return str(self.unique_key) + " " + str(self.Дата) + " " +  str(self.Вопрос)

    class Meta:
        verbose_name = "Список_ответов"
        verbose_name_plural = "Список_ответов"
        

class Список_ПВИ(models.Model):
    Название_ПВИ = models.CharField(max_length=200)
    Местонахождение_ПВИ = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Название_ПВИ)

    class Meta:
        verbose_name = "Список_ПВИ"
        verbose_name_plural = "Список_ПВИ"

class Дата_окончания_голосования(models.Model):
    Дата = models.DateField()

    def __str__(self):
        return str(self.Дата)

    class Meta:
        verbose_name = "Дата_окончания_голосования"
        verbose_name_plural = "Дата_окончания_голосования"

class Общие_комментарии(models.Model):
    unique_key = models.IntegerField()
    Пожелание = models.TextField()

    def __str__(self):
        return str(self.unique_key)

    class Meta:
        verbose_name = "Общие_комментарии"
        verbose_name_plural = "Общие_комментарии"