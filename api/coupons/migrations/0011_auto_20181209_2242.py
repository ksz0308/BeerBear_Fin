# Generated by Django 2.1.2 on 2018-12-09 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0010_auto_20181209_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 9, 22, 42, 57, 437522)),
        ),
    ]