# Generated by Django 3.2.5 on 2021-08-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0011_staticsarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticsarticle',
            name='error_text',
            field=models.CharField(default=None, max_length=50, verbose_name='Your Browser Does Not Support HTML5 (text)'),
        ),
    ]
