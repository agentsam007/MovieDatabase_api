# Generated by Django 2.2.5 on 2019-11-08 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='MovieList',
        ),
    ]
