# Generated by Django 2.0.6 on 2018-06-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180610_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='processor',
            field=models.CharField(max_length=20),
        ),
    ]
