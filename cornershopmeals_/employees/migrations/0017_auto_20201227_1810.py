# Generated by Django 3.1.4 on 2020-12-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_auto_20201227_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(editable=False, help_text='Employee id.', primary_key=True, serialize=False),
        ),
    ]
