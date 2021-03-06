# Generated by Django 2.1.3 on 2019-03-01 02:10

from django.db import migrations
import faicon.fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20190228_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='icon',
            field=faicon.fields.FAIconField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='icon',
            field=faicon.fields.FAIconField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
