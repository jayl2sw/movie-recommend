# Generated by Django 3.2.12 on 2022-05-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0007_alter_collection_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default='아아 디스크립션을 빼먹었습니다. 이건 테스트용입니다.'),
            preserve_default=False,
        ),
    ]