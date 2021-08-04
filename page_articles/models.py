from django.db import models


class Log(models.Model):
    lang = models.CharField(verbose_name="Language (as TR or EN)", max_length=2)
    log_date = models.CharField(verbose_name="Log Date", max_length=25)
    search = models.CharField(verbose_name="Search", max_length=25)
    page = models.CharField(verbose_name="Page", max_length=25)
    go = models.CharField(verbose_name="Go", max_length=25)
    level = models.CharField(verbose_name="Level", max_length=25)
    source = models.CharField(verbose_name="Source", max_length=25)
    date = models.CharField(verbose_name="Date", max_length=25)
    time = models.CharField(verbose_name="Time", max_length=25)
    data = models.CharField(verbose_name="Data", max_length=25)
    no_log = models.CharField(verbose_name="No Log Available", max_length=25)

    def __str__(self):
        return self.lang
