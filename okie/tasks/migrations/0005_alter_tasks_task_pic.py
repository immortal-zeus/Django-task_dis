# Generated by Django 3.2.3 on 2021-05-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210528_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]