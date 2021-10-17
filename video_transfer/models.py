from django.db import models


class GeneralSettings(models.Model):
  codec_types = [
    ("0", "flv"),
    ("1", "avi"),
    ("2", "hls"),
    ("3", "ogg"),
    ("4", "mpeg4"),
    ("5", "gif"),
    ("6", "jpeg2000")
  ]
  udp_comm_ip_address = models.GenericIPAddressField(verbose_name="udp_comm_ip_address")
  udp_comm_port = models.IntegerField(verbose_name="udp_comm_port")
  video_frame_rate = models.IntegerField(verbose_name="video_frame_rate (fps)")
  video_codec_type = models.CharField(verbose_name="video_codec_type", max_length=10, choices=codec_types)
  video_tune = models.CharField(verbose_name="video_tune", max_length=15, default=None)

  def __str__(self):
    return "General Setting"


class InputSettings(models.Model):
  protocols = [
    ("0", "rtsp"),
    ("1", "rtp"),
    ("2", "rtmp"),
    ("3", "mpeg"),
    ("4", "srt"),
    ("5", "hls")
  ]
  input_protocol = models.CharField(verbose_name="input_protocol", max_length=5, choices=protocols)
  input_url = models.CharField(verbose_name="input_url", max_length=30)

  def __str__(self):
      return "Input Settings"


class OutputSettings(models.Model):
  protocols = [
    ("0", "rtsp"),
    ("1", "rtp"),
    ("2", "rtmp"),
    ("3", "mpeg"),
    ("4", "srt"),
    ("5", "hls")
  ]
  video_formats = [
    ("0", "flv"),
    ("1", "avi"),
    ("2", "hls"),
    ("3", "ogg"),
    ("4", "mpeg4"),
    ("5", "gif"),
    ("6", "jpeg2000")
  ]
  audio_format = [
    ("0", "vpx"),
    ("1", "h264"),
    ("2", "h265"),
    ("3", "avs2")
  ]
  output_protocol = models.CharField(verbose_name="output_protocol", max_length=5, choices=protocols)
  output_url = models.CharField(verbose_name="output_url", max_length=30)
  output_audio_format = models.CharField(verbose_name="output_audio_format", max_length=5, choices=audio_format)
  output_video_format = models.CharField(verbose_name="output_video_format", max_length=9, choices=video_formats)

  def __str__(self):
      return "Output Settings"
