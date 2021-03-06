# Generated by Django 2.1.2 on 2018-12-02 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('is_used', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('count', models.IntegerField()),
                ('due_date', models.DateTimeField(default=datetime.datetime(2019, 3, 2, 13, 42, 26, 211212))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
