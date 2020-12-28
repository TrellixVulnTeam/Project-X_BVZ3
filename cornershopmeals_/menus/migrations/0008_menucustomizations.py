# Generated by Django 3.1.4 on 2020-12-27 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20201227_1802'),
        ('menus', '0007_delete_menucustomizations'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCustomizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization_text', models.CharField(help_text='Employee customizations', max_length=500, null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
            ],
            options={
                'db_table': 'menu_customizations',
            },
        ),
    ]