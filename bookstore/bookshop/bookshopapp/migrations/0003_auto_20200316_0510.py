# Generated by Django 2.1.7 on 2020-03-16 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshopapp', '0002_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='bookid',
        ),
        migrations.RemoveField(
            model_name='log',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
