# Generated by Django 3.0.2 on 2021-02-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0028_gpscheckin_monitor_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='iap_apple_blurb',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='paying',
            field=models.BooleanField(default=False),
        ),
    ]
