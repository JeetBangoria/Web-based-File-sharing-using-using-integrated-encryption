# Generated by Django 3.0 on 2020-11-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20201104_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file_name',
            field=models.TextField(default='filename'),
        ),
    ]
