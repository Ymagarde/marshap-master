# Generated by Django 2.2.3 on 2019-08-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0023_auto_20190809_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='source',
            field=models.CharField(default='', max_length=500),
        ),
    ]
