# Generated by Django 4.2.5 on 2023-09-14 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_contactapp_new_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactapp',
            name='new_slug',
        ),
    ]
