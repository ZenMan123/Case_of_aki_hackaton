# Generated by Django 4.2.1 on 2023-05-23 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_emailverification_email_and_more'),
        ('clients', '0005_client_email_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_verification',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.emailverification'),
        ),
    ]
