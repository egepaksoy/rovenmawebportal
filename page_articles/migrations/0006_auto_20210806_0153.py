# Generated by Django 3.2.5 on 2021-08-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_articles', '0005_auto_20210806_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalAccessArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2, verbose_name='Language (like TR or EN)')),
                ('title', models.CharField(max_length=35, verbose_name='Local Access Settings (title)')),
                ('dhcp', models.CharField(max_length=30, verbose_name='Baud Rate (field)')),
                ('ip_address', models.CharField(max_length=25, verbose_name='Data Bits (field)')),
                ('port', models.CharField(max_length=25, verbose_name='Stop Bits (field)')),
                ('subnet_mask', models.CharField(max_length=50, verbose_name='Parity (field)')),
                ('now_text', models.CharField(max_length=25, verbose_name='Now')),
                ('save_text', models.CharField(max_length=25, verbose_name='Save (text)')),
            ],
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='data',
            field=models.CharField(max_length=25, verbose_name='Data (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='date',
            field=models.CharField(max_length=25, verbose_name='Date (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='go',
            field=models.CharField(max_length=25, verbose_name='Go (text)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='level',
            field=models.CharField(max_length=25, verbose_name='Level (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='log_date',
            field=models.CharField(max_length=25, verbose_name='Log Date (text)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='log_records',
            field=models.CharField(default=None, max_length=50, verbose_name='Log Dump Settings (title)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='no_log',
            field=models.CharField(max_length=25, verbose_name='No Log Available (text)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='page',
            field=models.CharField(max_length=25, verbose_name='Page (text)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='search',
            field=models.CharField(max_length=25, verbose_name='Search (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='source',
            field=models.CharField(max_length=25, verbose_name='Source (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='time',
            field=models.CharField(max_length=25, verbose_name='Time (field)'),
        ),
        migrations.AlterField(
            model_name='logarticles',
            name='type',
            field=models.CharField(default=None, max_length=25, verbose_name='Source Type (field)'),
        ),
    ]