# Generated by Django 2.1.3 on 2019-02-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190228_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='icon',
            field=models.ImageField(upload_to='icon/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='income',
            name='icon',
            field=models.ImageField(upload_to='icon/%Y/%m/%d'),
        ),
    ]
