# Generated by Django 3.2.6 on 2021-09-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_timesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='localaccesssettings',
            name='open_cli',
            field=models.BooleanField(default=None, verbose_name='Open CLI'),
        ),
    ]