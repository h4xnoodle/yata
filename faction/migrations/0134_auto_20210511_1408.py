# Generated by Django 3.1.5 on 2021-05-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0133_auto_20210410_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='revive',
            name='target_early_discharge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='revivesreport',
            name='include_early',
            field=models.BooleanField(default=True),
        ),
    ]
