# Generated by Django 3.2.5 on 2021-08-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0003_auto_20210805_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteAccessArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2, verbose_name='Language (like TR or EN)')),
                ('title', models.CharField(max_length=35, verbose_name='Remote Access Settings Title')),
                ('dhcp', models.CharField(max_length=30, verbose_name='DHCP Enabled/disabled')),
                ('ip_address', models.CharField(max_length=25, verbose_name='IP Address')),
                ('port', models.CharField(max_length=25, verbose_name='Port')),
                ('subnet_mask', models.CharField(default=None, max_length=50, verbose_name='Subnet Mask')),
                ('broadcast_address', models.CharField(max_length=25, verbose_name='Broadcast Address')),
                ('gateway_address', models.CharField(max_length=25, verbose_name='Gateway Address')),
                ('dns_address', models.CharField(default=None, max_length=25, verbose_name='DNS Address')),
                ('dhcp_address', models.CharField(max_length=25, verbose_name='DHCP Address')),
                ('save', models.CharField(max_length=25, verbose_name='Save')),
                ('enabled', models.CharField(max_length=25, verbose_name='Enabled')),
                ('disabled', models.CharField(max_length=25, verbose_name='Disabled')),
            ],
        ),
        migrations.RenameModel(
            old_name='Log',
            new_name='LogArticles',
        ),
        migrations.DeleteModel(
            name='RemoteAccess',
        ),
    ]
