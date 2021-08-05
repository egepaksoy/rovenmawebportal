# Generated by Django 3.2.5 on 2021-08-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0004_auto_20210806_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remoteaccessarticles',
            name='save',
        ),
        migrations.AddField(
            model_name='remoteaccessarticles',
            name='save_text',
            field=models.CharField(default=None, max_length=25, verbose_name='Save (text)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='broadcast_address',
            field=models.CharField(max_length=25, verbose_name='Broadcast Address (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='dhcp',
            field=models.CharField(max_length=30, verbose_name='DHCP Enabled/Disabled (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='dhcp_address',
            field=models.CharField(max_length=25, verbose_name='DHCP Address (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='disabled',
            field=models.CharField(max_length=25, verbose_name='Disabled (text)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='dns_address',
            field=models.CharField(default=None, max_length=25, verbose_name='DNS Address (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='enabled',
            field=models.CharField(max_length=25, verbose_name='Enabled (text)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='gateway_address',
            field=models.CharField(max_length=25, verbose_name='Gateway Address (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='ip_address',
            field=models.CharField(max_length=25, verbose_name='IP Address (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='port',
            field=models.CharField(max_length=25, verbose_name='Port (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='subnet_mask',
            field=models.CharField(default=None, max_length=50, verbose_name='Subnet Mask (field)'),
        ),
        migrations.AlterField(
            model_name='remoteaccessarticles',
            name='title',
            field=models.CharField(max_length=35, verbose_name='Remote Access Settings (title)'),
        ),
    ]
