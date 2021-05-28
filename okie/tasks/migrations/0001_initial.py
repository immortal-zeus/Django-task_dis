# Generated by Django 3.2.3 on 2021-05-27 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('join_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=200)),
                ('task_description', models.CharField(max_length=2000, null=True)),
                ('task_pic', models.ImageField(upload_to='taskimage/')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to='tasks.user')),
            ],
        ),
    ]