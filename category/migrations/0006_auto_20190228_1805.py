# Generated by Django 2.1.3 on 2019-02-28 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20190228_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='income',
            name='icon',
        ),
    ]
