# Generated by Django 4.2.1 on 2023-05-21 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('platforms', '0001_initial'),
        ('organizers', '0002_entry_client_entry_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.platform'),
        ),
    ]
