# Generated by Django 4.1 on 2022-08-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.IntegerField(default=1, verbose_name='Id пользователя телеграм'),
            preserve_default=False,
        ),
    ]