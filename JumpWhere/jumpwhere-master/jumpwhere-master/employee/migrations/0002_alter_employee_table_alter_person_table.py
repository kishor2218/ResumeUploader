# Generated by Django 4.2.7 on 2023-11-21 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
        migrations.AlterModelTable(
            name='person',
            table='user',
        ),
    ]
