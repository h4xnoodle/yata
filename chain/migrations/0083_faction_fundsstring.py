# Generated by Django 2.2.7 on 2019-12-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0082_faction_memberstatusupda'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='fundsString',
            field=models.TextField(default='{}'),
        ),
    ]