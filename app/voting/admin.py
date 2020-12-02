from django.contrib import admin
from .models import Список_вопросов, Список_ответов, Список_ПВИ, Дата_окончания_голосования, Общие_комментарии


@admin.register(Список_вопросов)
class Список_вопросовAdmin(admin.ModelAdmin):
    list_display = ("question_text", "date")

@admin.register(Список_ответов)
class Список_ответовAdmin(admin.ModelAdmin):
    list_display = ("unique_key", "Вопрос" ,"ПВИ", "Дата", "Оценка", )
    list_filter = ("ПВИ", "Вопрос" , "Оценка", "Дата")

@admin.register(Список_ПВИ)
class Список_ПВИAdmin(admin.ModelAdmin):
    list_display = ("Название_ПВИ", "Местонахождение_ПВИ")

@admin.register(Дата_окончания_голосования)
class Дата_окончания_голосованияAdmin(admin.ModelAdmin):
    pass

@admin.register(Общие_комментарии)
class Общие_комментарииAdmin(admin.ModelAdmin):
    pass