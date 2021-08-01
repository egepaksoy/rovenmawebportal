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
