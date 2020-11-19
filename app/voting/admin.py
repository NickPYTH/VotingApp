from django.contrib import admin
from .models import Список_вопросов, Список_ответов, Список_ПВИ, Дата_окончания_голосования, Общие_комментарии
# Register your models here.


admin.site.register(Список_вопросов)
admin.site.register(Список_ответов)
admin.site.register(Список_ПВИ)
admin.site.register(Дата_окончания_голосования)
admin.site.register(Общие_комментарии)



