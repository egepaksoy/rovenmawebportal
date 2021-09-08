from django.db import models

class Ftp_settings(models.Model):
  supported_login_items = [
    ("0", "ftp"),
    ("1", "authpriv"),
    ("2", "deamon"),
    ("3", "auth"),
    ("4", "security"),
    ("5", "user"),
    ("6", "local"),
    ("None", "None")
  ]

  enable_pure_db = models.BooleanField(verbose_name="enable_pure_db")
  enable_pam = models.BooleanField(verbose_name="enable_pam")
  enable_ssl_cert = models.BooleanField(verbose_name="enable_ssl_cert")
  enable_verbose_log = models.BooleanField(verbose_name="enable_verbose_log")
  enable_no_anonymous = models.BooleanField(verbose_name="enable_no_anonymous")
  ssl_cert_path = models.CharField(verbose_name="ssl_cert_path", max_length=50)
  tls = models.SmallIntegerField(verbose_name="tls")
  tls_chiper_suite = models.CharField(verbose_name="tls_chiper_suite", max_length=50)
  supported_items = models.CharField(verbose_name="supported_items", max_length=9, choices=supported_login_items)
  syslog_facility_type = models.CharField(verbose_name="syslog_facility_type", choices=supported_login_items, max_length=9)
  pure_ftp_base_path = models.CharField(verbose_name="pure_ftp_base_path", max_length=30)
  pure_ftp_config_file = models.CharField(verbose_name="pure_ftp_config_file", max_length=30)
  max_clients_number = models.SmallIntegerField(verbose_name="max_clients_number")
  max_clients_per_ip = models.SmallIntegerField(verbose_name="max_clients_per_ip")

  def __str__(self):
      return "FTP Settings"