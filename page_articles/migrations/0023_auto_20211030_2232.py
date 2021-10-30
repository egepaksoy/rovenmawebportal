# Generated by Django 3.2.8 on 2021-10-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0022_navbarfooterarticles_packets'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticsarticle',
            name='cpu',
            field=models.CharField(default=None, max_length=15, null=True, verbose_name='CPU'),
        ),
        migrations.AddField(
            model_name='staticsarticle',
            name='free',
            field=models.CharField(default=None, max_length=10, null=True, verbose_name='Free'),
        ),
        migrations.AddField(
            model_name='staticsarticle',
            name='memory',
            field=models.CharField(default=None, max_length=15, null=True, verbose_name='Memory'),
        ),
        migrations.AddField(
            model_name='staticsarticle',
            name='now',
            field=models.CharField(default=None, max_length=10, null=True, verbose_name='Now'),
        ),
        migrations.AddField(
            model_name='staticsarticle',
            name='ssd',
            field=models.CharField(default=None, max_length=15, null=True, verbose_name='SSD'),
        ),
    ]