# Generated by Django 5.0.4 on 2024-04-09 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, default='Unknown', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='total_sell',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
