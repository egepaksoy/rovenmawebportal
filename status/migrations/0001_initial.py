# Generated by Django 3.2.5 on 2021-08-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50, verbose_name='Log Seviyesi')),
                ('source', models.CharField(max_length=50, verbose_name='Log Kaynağı')),
                ('type', models.CharField(max_length=50, verbose_name='Kaynak Tipi')),
                ('date', models.DateField(verbose_name='Log Tarihi')),
                ('time', models.TimeField(verbose_name='Log Saati')),
                ('data', models.TextField(max_length=1000, verbose_name='Log Verisi')),
            ],
        ),
    ]
