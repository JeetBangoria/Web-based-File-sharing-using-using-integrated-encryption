# Generated by Django 3.1.2 on 2020-10-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='first_name',
            field=models.TextField(default=''),
        ),
    ]
