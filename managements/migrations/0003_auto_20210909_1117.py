# Generated by Django 3.1.13 on 2021-09-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0002_auto_20210909_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='fcm_token',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
