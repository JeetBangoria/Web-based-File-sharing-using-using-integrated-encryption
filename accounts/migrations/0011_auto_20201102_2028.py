# Generated by Django 3.0 on 2020-11-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201102_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file_upload',
            field=models.TextField(blank=True, db_column='data'),
        ),
    ]
