# Generated by Django 2.2.16 on 2022-07-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0058_organization_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
