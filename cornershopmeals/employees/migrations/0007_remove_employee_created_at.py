# Generated by Django 3.1.4 on 2020-12-27 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20201227_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
    ]