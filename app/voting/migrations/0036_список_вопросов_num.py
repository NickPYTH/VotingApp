# Generated by Django 3.1.3 on 2020-11-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0035_auto_20201130_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='список_вопросов',
            name='num',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
