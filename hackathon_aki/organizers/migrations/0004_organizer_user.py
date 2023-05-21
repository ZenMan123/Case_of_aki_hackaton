# Generated by Django 4.2.1 on 2023-05-21 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizers', '0003_alter_entry_client_alter_entry_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]