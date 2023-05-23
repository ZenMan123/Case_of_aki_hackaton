# Generated by Django 4.2.1 on 2023-05-23 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_emailverification_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverification',
            options={'verbose_name': 'Не подтверждённый аккаунт', 'verbose_name_plural': 'Не подтверждённые аккаунты'},
        ),
        migrations.AddField(
            model_name='emailverification',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailverification',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailverification',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=254, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailverification',
            name='verification_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=254, unique=True, verbose_name='Код подтверждения'),
            preserve_default=False,
        ),
    ]