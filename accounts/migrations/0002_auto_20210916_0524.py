# Generated by Django 3.1.13 on 2021-09-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='avatar.png', upload_to='media/'),
        ),
    ]
