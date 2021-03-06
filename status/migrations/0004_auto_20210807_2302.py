# Generated by Django 3.2.5 on 2021-08-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20210807_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statics',
            name='cpu_now',
            field=models.FloatField(verbose_name='CPU Now'),
        ),
        migrations.AlterField(
            model_name='statics',
            name='cpu_top',
            field=models.FloatField(verbose_name='CPU Top'),
        ),
        migrations.AlterField(
            model_name='statics',
            name='memory_now',
            field=models.IntegerField(verbose_name='Memory Now'),
        ),
        migrations.AlterField(
            model_name='statics',
            name='memory_top',
            field=models.IntegerField(verbose_name='Memory Top'),
        ),
    ]
