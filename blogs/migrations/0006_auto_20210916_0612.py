# Generated by Django 3.1.13 on 2021-09-16 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20210916_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
