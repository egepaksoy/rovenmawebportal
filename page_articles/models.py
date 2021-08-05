from django.db import models


class LogArticles(models.Model):
    lang = models.CharField(verbose_name="Language (like TR or EN)", max_length=2)
    log_date = models.CharField(verbose_name="Log Date (text)", max_length=25)
    search = models.CharField(verbose_name="Search (field)", max_length=25)
    page = models.CharField(verbose_name="Page (text)", max_length=25)
    go = models.CharField(verbose_name="Go (text)", max_length=25)
    log_records = models.CharField(verbose_name="Log Dump Settings (title)", max_length=50, default=None)
    level = models.CharField(verbose_name="Level (field)", max_length=25)
    source = models.CharField(verbose_name="Source (field)", max_length=25)
    type = models.CharField(verbose_name="Source Type (field)", max_length=25, default=None)
    date = models.CharField(verbose_name="Date (field)", max_length=25)
    time = models.CharField(verbose_name="Time (field)", max_length=25)
    data = models.CharField(verbose_name="Data (field)", max_length=25)
    no_log = models.CharField(verbose_name="No Log Available (text)", max_length=25)

    def __str__(self):
        return self.lang


class RemoteAccessArticles(models.Model):
    lang = models.CharField(verbose_name="Language (like TR or EN)", max_length=2)
    title = models.CharField(verbose_name="Remote Access Settings (title)", max_length=35)
    dhcp = models.CharField(verbose_name="DHCP Enabled/Disabled (field)", max_length=30)
    ip_address = models.CharField(verbose_name="IP Address (field)", max_length=25)
    port = models.CharField(verbose_name="Port (field)", max_length=25)
    subnet_mask = models.CharField(verbose_name="Subnet Mask (field)", max_length=50, default=None)
    broadcast_address = models.CharField(verbose_name="Broadcast Address (field)", max_length=25)
    gateway_address = models.CharField(verbose_name="Gateway Address (field)", max_length=25)
    dns_address = models.CharField(verbose_name="DNS Address (field)", max_length=25, default=None)
    dhcp_address = models.CharField(verbose_name="DHCP Address (field)", max_length=25)
    save_text = models.CharField(verbose_name="Save (text)", max_length=25, default=None)
    enabled = models.CharField(verbose_name="Enabled (text)", max_length=25)
    disabled = models.CharField(verbose_name="Disabled (text)", max_length=25)

    def __str__(self):
        return self.lang


class LocalAccessArticles(models.Model):
    lang = models.CharField(verbose_name="Language (like TR or EN)", max_length=2)
    title = models.CharField(verbose_name="Local Access Settings (title)", max_length=35)
    baud_rate = models.CharField(verbose_name="Baud Rate (field)", max_length=30)
    data_bits = models.CharField(verbose_name="Data Bits (field)", max_length=25)
    stop_bits = models.CharField(verbose_name="Stop Bits (field)", max_length=25)
    parity_text = models.CharField(verbose_name="Parity (field)", max_length=50)
    now_text = models.CharField(verbose_name="Now", max_length=25)
    save_text = models.CharField(verbose_name="Save (text)", max_length=25)

    def __str__(self):
        return self.lang

