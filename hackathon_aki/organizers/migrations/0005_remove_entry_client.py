# Generated by Django 4.2.1 on 2023-05-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0004_entry_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='client',
        ),
    ]