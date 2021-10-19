from django.db import models


class RemoteAccessSettings(models.Model):
    dhcp_enabled = models.BooleanField(verbose_name="DHCP Disabled")
    ip_address = models.GenericIPAddressField(verbose_name="IP Address")
    port = models.IntegerField(verbose_name="Port")
    subnet_mask = models.GenericIPAddressField(verbose_name="Subnet Mask")
    broadcast_address = models.GenericIPAddressField(verbose_name="Broadcast Address")
    gateway_address = models.GenericIPAddressField(verbose_name="Gateway Address")
    dns_address = models.GenericIPAddressField(verbose_name="DNS Address")
    dhcp_address = models.GenericIPAddressField(verbose_name="DHCP Address")
    open_remote = models.BooleanField(verbose_name="Enable Remote Access", default=None, null=False)

    def __str__(self):
        return "RemoteAccessSettings"


class LocalAccessSettings(models.Model):
    baud_rate = models.IntegerField(verbose_name="Baud Rate")
    data_bits = models.IntegerField(verbose_name="Data Bits")
    stop_bits = models.IntegerField(verbose_name="Stop Bits")
    parity = models.CharField(verbose_name="Parity Field", max_length=50)
    open_cli = models.BooleanField(verbose_name="Open CLI", default=None)

    def __str__(self):
        return "LocalAddressSettings"


class TimeSettings(models.Model):
    TIMEZONES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
        ("19", "19"),
        ("20", "20"),
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24")
    ]

    use_ntp = models.BooleanField(verbose_name="Use NTP")
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    server1 = models.CharField(verbose_name="Server 1", max_length=200)
    server2 = models.CharField(verbose_name="Server 2", max_length=200)
    timezone = models.CharField(verbose_name="Timezone", max_length=2, choices=TIMEZONES, default=0)

    def __str__(self):
        return "TimeSettings"
