# Generated by Django 2.2.3 on 2019-07-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0016_userprofileinfo_user_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='is_monitor_user',
            field=models.BooleanField(default=False),
        ),
    ]
