# Generated by Django 3.1.5 on 2021-02-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0058_delete_assist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('wars', models.TextField(default='{}')),
            ],
        ),
    ]
