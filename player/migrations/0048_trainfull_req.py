# Generated by Django 3.0.4 on 2020-05-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0047_auto_20200504_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainfull',
            name='req',
            field=models.TextField(default='{}'),
        ),
    ]