# Generated by Django 2.0.5 on 2019-08-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0052_count_warhits'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='poster',
            field=models.BooleanField(default=False),
        ),
    ]
