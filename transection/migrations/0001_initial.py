# Generated by Django 2.1.5 on 2019-02-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('income', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
