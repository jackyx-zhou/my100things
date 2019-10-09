# Generated by Django 2.2.5 on 2019-10-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20190930_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='type',
            field=models.CharField(choices=[('Top', (('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('jacket', 'jacket'), ('hoodie', 'hoodie'), ('jumper', 'jumper'), ('other', 'other'))), ('Trousers', (('jeans', 'jeans'), ('joggers', 'joggers'), ('other', 'other'))), ('shorts', 'shorts'), ('underwear', 'underwear'), ('socks', 'socks'), ('accessory', 'accessory'), ('other', 'other')], max_length=15),
        ),
    ]
