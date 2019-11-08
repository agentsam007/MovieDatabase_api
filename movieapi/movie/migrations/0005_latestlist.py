# Generated by Django 2.2.5 on 2019-11-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_popularlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('popularity', models.FloatField()),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
