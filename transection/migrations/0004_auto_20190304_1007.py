# Generated by Django 2.1.3 on 2019-03-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transection', '0003_auto_20190304_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transection',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
