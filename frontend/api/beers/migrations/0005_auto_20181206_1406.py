# Generated by Django 2.1.2 on 2018-12-06 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_auto_20181202_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beerreview',
            options={'ordering': ['-created_at']},
        ),
    ]
