# Generated by Django 3.2.8 on 2021-10-23 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0007_rename_area_temprature_sensors_reciever_temprature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensors',
            old_name='data_temprature',
            new_name='transmitter_temprature',
        ),
    ]
