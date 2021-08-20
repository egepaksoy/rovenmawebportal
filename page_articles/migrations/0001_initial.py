# Generated by Django 3.2.5 on 2021-08-04 18:18

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
                ('lang', models.CharField(max_length=2, verbose_name='Language (as TR or EN)')),
                ('log_date', models.CharField(max_length=25, verbose_name='Log Date')),
                ('search', models.CharField(max_length=25, verbose_name='Search')),
                ('page', models.CharField(max_length=25, verbose_name='Page')),
                ('go', models.CharField(max_length=25, verbose_name='Go')),
                ('level', models.CharField(max_length=25, verbose_name='Level')),
                ('source', models.CharField(max_length=25, verbose_name='Source')),
                ('date', models.CharField(max_length=25, verbose_name='Date')),
                ('time', models.CharField(max_length=25, verbose_name='Time')),
                ('data', models.CharField(max_length=25, verbose_name='Data')),
                ('no_log', models.CharField(max_length=25, verbose_name='No Log Available')),
            ],
        ),
    ]
