# Generated by Django 3.0 on 2020-11-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('public_keyX', models.TextField()),
                ('public_keyY', models.TextField()),
            ],
        ),
    ]
