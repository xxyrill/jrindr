# Generated by Django 5.0.6 on 2024-06-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
