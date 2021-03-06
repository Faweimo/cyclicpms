# Generated by Django 3.1.13 on 2021-09-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210822_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='unsplash.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
