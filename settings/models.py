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
