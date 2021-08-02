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

    def __str__(self):
        return "RemoteAccessSettings"


class LocalAccessSettings(models.Model):
    baud_rate = models.IntegerField(verbose_name="Baud Rate")
    data_bits = models.IntegerField(verbose_name="Data Bits")
    stop_bits = models.IntegerField(verbose_name="Stop Bits")
    parity = models.CharField(verbose_name="Parity Field", max_length=50)

    def __str__(self):
        return "LocalAddressSettings"

