from django.db import models


class LogArticles(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    log_date = models.CharField(verbose_name="Log Date (text)", max_length=25)
    search = models.CharField(verbose_name="Search (field)", max_length=25)
    page = models.CharField(verbose_name="Page (text)", max_length=25)
    go = models.CharField(verbose_name="Go (text)", max_length=25)
    log_records = models.CharField(
        verbose_name="Log Dump Settings (title)", max_length=50, default=None)
    level = models.CharField(verbose_name="Level (field)", max_length=25)
    source = models.CharField(verbose_name="Source (field)", max_length=25)
    type = models.CharField(
        verbose_name="Source Type (field)", max_length=25, default=None)
    date = models.CharField(verbose_name="Date (field)", max_length=25)
    time = models.CharField(verbose_name="Time (field)", max_length=25)
    data = models.CharField(verbose_name="Data (field)", max_length=25)
    no_log = models.CharField(
        verbose_name="No Log Available (text)", max_length=25)

    def __str__(self):
        return self.lang


class RemoteAccessArticles(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    title = models.CharField(
        verbose_name="Remote Access Settings (title)", max_length=35)
    dhcp = models.CharField(
        verbose_name="DHCP Enabled/Disabled (field)", max_length=30)
    ip_address = models.CharField(
        verbose_name="IP Address (field)", max_length=25)
    port = models.CharField(verbose_name="Port (field)", max_length=25)
    subnet_mask = models.CharField(
        verbose_name="Subnet Mask (field)", max_length=50, default=None)
    broadcast_address = models.CharField(
        verbose_name="Broadcast Address (field)", max_length=25)
    gateway_address = models.CharField(
        verbose_name="Gateway Address (field)", max_length=25)
    dns_address = models.CharField(
        verbose_name="DNS Address (field)", max_length=25, default=None)
    dhcp_address = models.CharField(
        verbose_name="DHCP Address (field)", max_length=25)
    save_text = models.CharField(
        verbose_name="Save (text)", max_length=25, default=None)
    enabled = models.CharField(verbose_name="Enabled (text)", max_length=25)
    disabled = models.CharField(verbose_name="Disabled (text)", max_length=25)

    def __str__(self):
        return self.lang


class LocalAccessArticles(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    title = models.CharField(
        verbose_name="Local Access Settings (title)", max_length=35)
    baud_rate = models.CharField(
        verbose_name="Baud Rate (field)", max_length=30)
    data_bits = models.CharField(
        verbose_name="Data Bits (field)", max_length=25)
    stop_bits = models.CharField(
        verbose_name="Stop Bits (field)", max_length=25)
    parity_text = models.CharField(
        verbose_name="Parity (field)", max_length=50)
    now_text = models.CharField(verbose_name="Now", max_length=25)
    open_cli_access_switch = models.CharField(verbose_name="Open CLI Access (switch)", max_length=20, default=None)
    open_cli_access_info_text = models.CharField(verbose_name="Open CLI Access (info text)", max_length=70, default=None)
    save_text = models.CharField(verbose_name="Save (text)", max_length=25)

    def __str__(self):
        return self.lang


class TimeSettingsArticles(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    title = models.CharField(
        verbose_name="Time Settings (title)", max_length=35)
    ntp_enabled = models.CharField(
        verbose_name="NTP Enabled/Disabled (field)", max_length=30)
    date_time_field = models.CharField(
        verbose_name="Date and Time (field)", max_length=25)
    server_field = models.CharField(
        verbose_name="Server (field)", max_length=25)
    ip_address = models.CharField(
        verbose_name="IP Address (field)", max_length=50)
    timezone = models.CharField(verbose_name="Timezone (field)", max_length=25)
    enabled = models.CharField(verbose_name="Enabled (text)", max_length=25)
    disabled = models.CharField(verbose_name="Disabled (text)", max_length=25)
    save_text = models.CharField(verbose_name="Save (text)", max_length=25)

    def __str__(self):
        return self.lang


class UserAdministration(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    user_administration = models.CharField(
        verbose_name="User Administration (page title)", max_length=35)
    user_create_title = models.CharField(
        verbose_name="User Create (title)", max_length=35)
    user_name_surname = models.CharField(
        verbose_name="Name Surname (field)", max_length=35)
    username = models.CharField(verbose_name="Username (field)", max_length=25)
    password = models.CharField(verbose_name="Password (field)", max_length=25)
    confirm_password = models.CharField(
        verbose_name="Confirm Password (field)", max_length=30)
    authority_status = models.CharField(
        verbose_name="Authority Status (field)", max_length=25)
    create_user = models.CharField(verbose_name="Create (text)", max_length=25)
    user_settings = models.CharField(
        verbose_name="User Settings (title)", max_length=35)
    delete = models.CharField(verbose_name="Delete (field)", max_length=20)

    def __str__(self):
        return self.lang


class NavbarFooterArticles(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    homepage = models.CharField(verbose_name="Home (link)", max_length=20)
    system_status = models.CharField(
        verbose_name="System Status (dropdown)", max_length=30)
    statistics_field = models.CharField(
        verbose_name="Statistics (field)", max_length=20)
    sensors = models.CharField(verbose_name="Sensors (field)", max_length=20)
    log_records = models.CharField(
        verbose_name="Log Records (field)", max_length=30)
    system_settings = models.CharField(
        verbose_name="System Settings (dropdown)", max_length=30)
    remote_access_settings = models.CharField(
        verbose_name="Remote Access Settings (field)", max_length=35)
    cli_access_settings = models.CharField(
        verbose_name="CLI Access Settings (field)", max_length=35)
    time_settings = models.CharField(
        verbose_name="Time Settings (field)", max_length=35)
    user_settings = models.CharField(
        verbose_name="User Settings (dropdown)", max_length=35)
    user_administration = models.CharField(
        verbose_name="User Administration (field)", max_length=30)
    authorization = models.CharField(
        verbose_name="Authorization (field)", max_length=35)
    password_changing = models.CharField(
        verbose_name="Password Changing (field)", max_length=35)
    video_transfer = models.CharField(
        verbose_name="Video Transfer Settings (dropdown)", max_length=35, default=None, null=True)
    video_transfer_settings = models.CharField(
        verbose_name="Settings (field)", max_length=15, default=None, null=True)
    input_settings = models.CharField(
        verbose_name="Input Settings (field)", max_length=18, default=None, null=True)
    ftp_settings = models.CharField(
        verbose_name="FTP Settings (field)", max_length=15, default=None, null=True)
    logout_link = models.CharField(verbose_name="Logout (link)", max_length=20)
    footer = models.CharField(
        verbose_name="All Rights Reserved (text)", max_length=35)

    def __str__(self):
        return self.lang


class StaticsArticle(models.Model):
    lang = models.CharField(
        verbose_name="Language (like TR or EN)", max_length=2)
    package_title = models.CharField(
        verbose_name="Encrypted Packets (title)", max_length=25)
    package_pcs = models.CharField(verbose_name="Pcs (field)", max_length=25)
    package_last_packs = models.CharField(
        verbose_name="Number of last packs (text)", max_length=40)
    error_text = models.CharField(
        verbose_name="Your Browser Does Not Support HTML5 (text)", max_length=50, default=None)

    def __str__(self):
        return self.lang


class PacketsTitles(models.Model):
    lang = models.CharField(verbose_name="Language (like TR or EN)", max_length=2)
    management_port_incoming = models.CharField(verbose_name="Management Port Incoming (title)", max_length=30)
    management_port_outgoing = models.CharField(verbose_name="Management Port Outgoing (title)", max_length=30)
    one_way_port_incoming = models.CharField(verbose_name="One Way Port Incoming (title)", max_length=30)
    one_way_port_outgoing = models.CharField(verbose_name="One Way Port Outgoing (title)", max_length=30)

    def __str__(self):
        return self.lang
