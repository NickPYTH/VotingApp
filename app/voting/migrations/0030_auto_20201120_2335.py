# Generated by Django 3.1.3 on 2020-11-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0029_auto_20201120_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='список_ответов',
            name='unique_key',
            field=models.IntegerField(),
        ),
    ]
