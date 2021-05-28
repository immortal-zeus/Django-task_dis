# Generated by Django 3.2.3 on 2021-05-27 16:27

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_pic',
            field=models.ImageField(null=True, upload_to='taskimage/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, validators=[tasks.models.valid_username]),
        ),
    ]
