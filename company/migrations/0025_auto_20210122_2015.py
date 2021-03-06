# Generated by Django 3.1.5 on 2021-01-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0024_companystock_delta_sold_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='lastw_customers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='lastw_income',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='lastw_profit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companydata',
            name='lastw_customers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companydata',
            name='lastw_income',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companydata',
            name='lastw_profit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='daily_profit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='weekly_profit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='daily_profit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='weekly_profit',
            field=models.BigIntegerField(default=0),
        ),
    ]
