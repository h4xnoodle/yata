# Generated by Django 3.0.1 on 2020-02-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0028_auto_20200202_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news',
            field=models.CharField(default='news', max_length=512),
        ),
    ]
