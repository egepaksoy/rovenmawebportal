# Generated by Django 3.2.5 on 2021-08-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0007_auto_20210806_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSettingsArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2, verbose_name='Language (like TR or EN)')),
                ('title', models.CharField(max_length=35, verbose_name='Time Settings (title)')),
                ('ntp_enabled', models.CharField(max_length=30, verbose_name='NTP Enabled/Disabled (field)')),
                ('date_time_field', models.CharField(max_length=25, verbose_name='Date And Time (field)')),
                ('server_field', models.CharField(max_length=25, verbose_name='Server (field)')),
                ('ip_address', models.CharField(max_length=50, verbose_name='IP Address (field)')),
                ('timezone', models.CharField(max_length=25, verbose_name='Timezone')),
                ('enabled', models.CharField(max_length=25, verbose_name='Enabled (text)')),
                ('disabled', models.CharField(max_length=25, verbose_name='Disabled (text)')),
                ('save_text', models.CharField(max_length=25, verbose_name='Save (text)')),
            ],
        ),
    ]
