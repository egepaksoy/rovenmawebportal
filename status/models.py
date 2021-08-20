from django.db import models


class Log(models.Model):
    level = models.CharField(verbose_name="Log Seviyesi", max_length=50)
    source = models.CharField(verbose_name="Log Kaynağı", max_length=50)
    type = models.CharField(verbose_name="Kaynak Tipi", max_length=50)
    date = models.DateField(verbose_name="Log Tarihi")
    time = models.TimeField(verbose_name="Log Saati")
    data = models.TextField(verbose_name="Log Verisi", max_length=1000)

    def __str__(self):
        return self.level


class Statics(models.Model):
    memory_top = models.IntegerField(verbose_name="Memory Top")
    memory_now = models.IntegerField(verbose_name="Memory Now")
    cpu_top = models.FloatField(verbose_name="CPU Top")
    cpu_now = models.FloatField(verbose_name="CPU Now")
    ssd_top = models.IntegerField(verbose_name="SSD Top")
    ssd_now = models.IntegerField(verbose_name="SSD Now")
    packet_count = models.IntegerField(verbose_name="Packet Count")

    def __str__(self):
        return "Statics Data"

