# Generated by Django 3.1.3 on 2020-11-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0034_auto_20201122_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='список_вопросов',
            name='id',
        ),
    ]
