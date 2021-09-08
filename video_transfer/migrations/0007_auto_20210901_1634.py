# Generated by Django 3.2.6 on 2021-09-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transfer', '0006_alter_inputsettings_input_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutputSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_protocol', models.CharField(choices=[('0', 'rtsp'), ('1', 'rtp'), ('2', 'rtmp'), ('3', 'mpeg'), ('4', 'srt'), ('5', 'hls')], max_length=5, verbose_name='output_protocol')),
                ('output_url', models.CharField(max_length=30, verbose_name='output_url')),
                ('output_audio_format', models.CharField(choices=[('0', 'rtsp'), ('1', 'rtp'), ('2', 'rtmp'), ('3', 'mpeg'), ('4', 'srt'), ('5', 'hls')], max_length=5, verbose_name='output_audio_format')),
                ('output_video_format', models.CharField(choices=[('0', 'rtsp'), ('1', 'rtp'), ('2', 'rtmp'), ('3', 'mpeg'), ('4', 'srt'), ('5', 'hls')], max_length=5, verbose_name='output_video_format')),
            ],
        ),
        migrations.AlterField(
            model_name='inputsettings',
            name='input_protocol',
            field=models.CharField(choices=[('0', 'rtsp'), ('1', 'rtp'), ('2', 'rtmp'), ('3', 'mpeg'), ('4', 'srt'), ('5', 'hls')], max_length=5, verbose_name='input_protocol'),
        ),
    ]
