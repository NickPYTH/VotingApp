# Generated by Django 3.1.3 on 2020-11-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0021_remove_список_вопросов_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='список_вопросов',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='список_ответов',
            name='Дата',
            field=models.DateField(auto_now=True),
        ),
    ]
