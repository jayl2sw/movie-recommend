# Generated by Django 3.2.12 on 2022-05-19 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_followings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]