from django.db import models


class Authorization(models.Model):
    user_type = models.CharField(verbose_name="User Type (admin/operator/superadmin", max_length=10)
    user_administration_access = models.BooleanField(verbose_name="User Administration Access", default=None)
    user_administration_change = models.BooleanField(verbose_name="User Administration Change", default=None)

    def __str__(self):
        return self.user_type
