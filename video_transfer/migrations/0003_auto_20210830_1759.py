# Generated by Django 3.2.6 on 2021-08-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transfer', '0002_alter_generalsettings_video_codec_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsettings',
            name='video_tune',
            field=models.CharField(default=None, max_length=15, verbose_name='video_tune'),
        ),
        migrations.AlterField(
            model_name='generalsettings',
            name='video_codec_type',
            field=models.CharField(choices=[('flv', '0'), ('avi', '1'), ('hls', '2'), ('ogg', '3'), ('mpeg4', '4'), ('gif', '5'), ('jpeg2000', '6'), ('vpx', '7'), ('h264', '8'), ('h265', '9'), ('avs2', '10')], max_length=10, verbose_name='video_codec_type'),
        ),
    ]
