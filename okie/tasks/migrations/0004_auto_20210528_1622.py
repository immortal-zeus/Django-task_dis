# Generated by Django 3.2.3 on 2021-05-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_user_tuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='taskimage/'),
        ),
    ]
