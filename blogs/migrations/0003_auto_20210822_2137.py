# Generated by Django 3.1.13 on 2021-08-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210820_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='unsplash.jpg', upload_to='blogs'),
        ),
    ]
