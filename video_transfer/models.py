from django.db import models


class GeneralSettings(models.Model):
  codec_types = [
    ("0", "flv"),
    ("1", "avi"),
    ("2", "hls"),
    ("3", "ogg"),
    ("4", "mpeg4"),
    ("5", "gif"),
    ("6", "jpeg2000"),
    ("7", "vpx"),
    ("8", "h264"),
    ("9", "h265"),
    ("10", "avs2")
  ]
  udp_comm_ip_address = models.GenericIPAddressField(verbose_name="udp_comm_ip_address")
  udp_comm_port = models.IntegerField(verbose_name="udp_comm_port")
  video_frame_rate = models.IntegerField(verbose_name="video_frame_rate (fps)")
  video_codec_type = models.CharField(verbose_name="video_codec_type", max_length=10, choices=codec_types)
  video_tune = models.CharField(verbose_name="video_tune", max_length=15, default=None)

  def __str__(self):
      return "General Setting"