# Generated by Django 3.2.6 on 2021-09-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0012_staticsarticle_error_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbarfooterarticles',
            name='ftp_settings',
            field=models.CharField(default=None, max_length=15, verbose_name='FTP Settings (field)'),
        ),
        migrations.AddField(
            model_name='navbarfooterarticles',
            name='input_settings',
            field=models.CharField(default=None, max_length=18, verbose_name='Input Settings (field)'),
        ),
        migrations.AddField(
            model_name='navbarfooterarticles',
            name='video_transfer',
            field=models.CharField(default=None, max_length=35, verbose_name='Video Transfer Settings (dropdown)'),
        ),
        migrations.AddField(
            model_name='navbarfooterarticles',
            name='video_transfer_settings',
            field=models.CharField(default=None, max_length=15, verbose_name='Settings (field)'),
        ),
    ]
