# Generated by Django 4.1.5 on 2023-01-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
