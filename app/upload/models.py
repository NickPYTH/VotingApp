from django.db import models

# Create your models here.

class Send(models.Model):
    email = models.EmailField()
    review = models.TextField()
    file = models.FileField(upload_to='.', blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"