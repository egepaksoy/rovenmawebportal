# Generated by Django 3.2.8 on 2021-10-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0019_remoteaccessarticles_open_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='open_remote',
            field=models.CharField(default=None, max_length=25, verbose_name='Open Remote Access'),
        ),
    ]
