# Generated by Django 3.1.5 on 2021-04-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0121_auto_20210404_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armoryreport',
            name='state_string',
            field=models.CharField(default='No reports', max_length=128),
        ),
    ]
