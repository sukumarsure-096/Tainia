# Generated by Django 3.0.8 on 2020-07-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
