# Generated by Django 2.2.7 on 2019-12-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20191216_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='stockAlerts',
            field=models.BooleanField(default=False),
        ),
    ]
