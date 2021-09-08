# Generated by Django 3.2.6 on 2021-09-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transfer', '0008_auto_20210901_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='video_codec_type',
            field=models.CharField(choices=[('0', 'flv'), ('1', 'avi'), ('2', 'hls'), ('3', 'ogg'), ('4', 'mpeg4'), ('5', 'gif'), ('6', 'jpeg2000')], max_length=10, verbose_name='video_codec_type'),
        ),
    ]
