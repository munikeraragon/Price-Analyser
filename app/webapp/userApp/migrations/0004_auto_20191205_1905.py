# Generated by Django 2.2.5 on 2019-12-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_auto_20191129_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemURL',
            field=models.CharField(max_length=500),
        ),
    ]