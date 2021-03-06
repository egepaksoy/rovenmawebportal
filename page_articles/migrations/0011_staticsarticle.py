# Generated by Django 3.2.5 on 2021-08-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0010_navbarfooterarticles'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2, verbose_name='Language (like TR or EN)')),
                ('package_title', models.CharField(max_length=25, verbose_name='Encrypted Packets (title)')),
                ('package_pcs', models.CharField(max_length=25, verbose_name='Pcs (field)')),
                ('package_last_packs', models.CharField(max_length=40, verbose_name='Number of last packs (text)')),
            ],
        ),
    ]
