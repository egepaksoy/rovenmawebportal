# Generated by Django 3.2.8 on 2021-10-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20211017_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesettings',
            name='timezone2',
        ),
        migrations.AddField(
            model_name='timesettings',
            name='timezone',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')], default=0, max_length=2, verbose_name='Timezone'),
        ),
    ]
