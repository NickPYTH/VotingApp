# Generated by Django 3.1.3 on 2020-11-14 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20201114_1936'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Question_list',
        ),
    ]
