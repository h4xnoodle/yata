# Generated by Django 2.0.5 on 2019-04-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_auto_20190426_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='awardsInfo',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='awardsJson',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='player',
            name='bazaarInfo',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='player',
            name='bazaarJson',
            field=models.TextField(default='{}'),
        ),
    ]
