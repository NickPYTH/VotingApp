# Generated by Django 3.1.3 on 2020-11-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0022_auto_20201115_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='список_вопросов',
            name='date',
            field=models.DateField(),
        ),
    ]
