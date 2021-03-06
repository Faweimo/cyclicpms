# Generated by Django 3.1.13 on 2021-09-09 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0002_auto_20210909_0703'),
        ('leave', '0004_auto_20210908_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.employee')),
            ],
            options={
                'verbose_name': 'Notification Employee',
                'verbose_name_plural': 'Notification Employees',
            },
        ),
    ]
