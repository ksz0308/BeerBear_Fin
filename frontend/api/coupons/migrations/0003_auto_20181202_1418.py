# Generated by Django 2.1.2 on 2018-12-02 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_coupon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 2, 14, 18, 49, 549462)),
        ),
    ]
